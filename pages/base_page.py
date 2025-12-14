from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import logging

log = logging.getLogger(__name__)


class BasePage:
    """Base page class with common methods for all page objects."""

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def navigate_to(self, url):
        """Navigate to a specific URL."""
        self.driver.get(url)

    def find_element(self, by, value, timeout=15):
        """Find element with explicit wait."""
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )

    def find_elements(self, by, value, timeout=15):
        """Find multiple elements with explicit wait."""
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, value))
        )
        return self.driver.find_elements(by, value)

    def click_element(self, by, value, timeout=15):
        """Click on element with explicit wait."""
        element = WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, value))
        )
        element.click()

    def input_text(self, by, value, text, timeout=15):
        """Input text into an element."""
        element = self.find_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

    def scroll_down(self, pixels):
        """Scroll down by specified pixels."""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(1)  # Wait for content to load after scroll

    def wait_for_page_load(self, timeout=2):
        """Wait for page to be fully loaded."""
        time.sleep(timeout)

    def take_screenshot(self, filename):
        """Take a screenshot and save it."""
        self.driver.save_screenshot(filename)
        log.info(f"Screenshot saved: {filename}")

