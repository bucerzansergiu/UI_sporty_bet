import pytest
import logging
from helpers.driver_helper import get_mobile_chrome_driver


# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


@pytest.fixture(scope="function")
def driver():
    """
    Pytest fixture that provides a mobile Chrome driver instance.
    Automatically quits the driver after test completion.
    """
    driver = get_mobile_chrome_driver()
    yield driver
    driver.quit()

