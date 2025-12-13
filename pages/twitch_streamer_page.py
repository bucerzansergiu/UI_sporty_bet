from pages.base_page import BasePage
import time


class TwitchStreamerPage(BasePage):
    """Page object for Twitch streamer page."""

    def __init__(self, driver):
        super().__init__(driver)

    def wait_for_page_to_load(self, wait_time=5):
        """Wait for streamer page to fully load."""
        time.sleep(wait_time)

    def take_page_screenshot(self, filename="screenshots/streamer_page.png"):
        """Take a screenshot of the streamer page."""
        self.take_screenshot(filename)

