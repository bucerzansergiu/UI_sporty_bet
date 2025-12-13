from pages.twitch_home_page import TwitchHomePage
from pages.twitch_search_results_page import TwitchSearchResultsPage
from pages.twitch_streamer_page import TwitchStreamerPage
import os
import logging

log = logging.getLogger(__name__)


class TestTwitchMobile:
    """Test class for Twitch mobile automation."""

    def test_search_and_select_streamer(self, driver):
        """
        Test that navigates to Twitch mobile, searches for Starcraft II,
        scrolls down twice, selects a random streamer, and takes a screenshot.
        """
        # Create screenshots directory if it doesn't exist
        if not os.path.exists("screenshots"):
            os.makedirs("screenshots")

        # Initialize page objects
        home_page = TwitchHomePage(driver)
        search_page = TwitchSearchResultsPage(driver)
        streamer_page = TwitchStreamerPage(driver)

        log.info("Step 1: Opening Twitch mobile homepage...")
        home_page.open()

        log.info("Step 2: Navigating to directory page...")
        home_page.navigate_to_directory()

        log.info("Step 3: Searching for 'Starcraft II'...")
        search_page.search_for_game("Starcraft II")

        log.info("Step 4: Scrolling down twice...")
        search_page.scroll_down_twice()

        log.info("Step 5: Selecting a random streamer...")
        search_page.select_random_streamer()

        log.info("Step 6: Waiting for streamer page to load...")
        streamer_page.wait_for_page_to_load()

        log.info("Step 7: Taking screenshot...")
        streamer_page.take_page_screenshot("screenshots/twitch_streamer.png")

        log.info("Test completed successfully!")

