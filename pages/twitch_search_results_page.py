from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pages.base_page import BasePage
import random
import time
import logging

log = logging.getLogger(__name__)


class TwitchSearchResultsPage(BasePage):
    """Page object for Twitch search results page."""

    # Locators
    SEARCH_INPUT = (By.CSS_SELECTOR, "input[type='search']")
    STREAMER_LINKS = (By.XPATH, "//a[starts-with(@href, '/') and string-length(@href) > 1]")

    def __init__(self, driver):
        super().__init__(driver)

    def search_for_game(self, game_name):
        """Input game name in search bar and press Enter to search."""
        search_input = self.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(game_name)
        search_input.send_keys(Keys.RETURN)
        self.wait_for_page_load()

    def scroll_down_twice(self):
        """Scroll down two times."""
        self.scroll_down(400)

        self.scroll_down(400)
        time.sleep(1)

    def select_random_streamer(self):
        """Select a random streamer from search results."""
        self.wait_for_page_load()

        streamers = self.find_elements(*self.STREAMER_LINKS)

        # Filter out main navigation pages only
        excluded = ['activity', 'home', 'directory', 'search']
        valid_streamers = [
            s for s in streamers
            if s.is_displayed()
            and s.get_attribute('href')
            and not any(ex in s.get_attribute('href') for ex in excluded)
        ]

        log.info(f"Found {len(valid_streamers)} valid links")

        # Pick a random one
        random_streamer = random.choice(valid_streamers)
        log.info(f"Selected: {random_streamer.get_attribute('href')}")

        # Click it
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", random_streamer)
        self.wait_for_page_load()
        self.driver.execute_script("arguments[0].click();", random_streamer)
