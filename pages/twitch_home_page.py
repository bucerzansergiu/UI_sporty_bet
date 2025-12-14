from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time
import logging

log = logging.getLogger(__name__)


class TwitchHomePage(BasePage):
    """Page object for Twitch mobile home page."""

    # Locators
    COOKIE_ACCEPT_BUTTON = (By.CSS_SELECTOR, "button[data-a-target='consent-banner-accept']")

    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://m.twitch.tv"
        self.directory_url = "https://m.twitch.tv/directory"

    def open(self):
        """Open Twitch mobile home page."""
        self.navigate_to(self.url)
        time.sleep(2)  # Wait for page to load
        self.handle_cookie_consent()

    def handle_cookie_consent(self):
        """Handle cookie consent popup if it appears."""
        try:
            print("Checking for cookie consent popup...")
            accept_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable(self.COOKIE_ACCEPT_BUTTON)
            )
            accept_button.click()
            print("Cookie consent accepted")
            time.sleep(1)  # Wait for popup to disappear
        except Exception as e:
            print("No cookie consent popup found or already accepted")

    def navigate_to_directory(self):
        """Navigate directly to the directory page."""
        log.info("Navigating to directory page...")
        self.navigate_to(self.directory_url)
        time.sleep(3)  # Wait for directory page to load
        log.info("Directory page loaded")

