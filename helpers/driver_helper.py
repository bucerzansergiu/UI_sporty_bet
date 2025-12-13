from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_mobile_chrome_driver():
    """
    Create and configure Chrome driver with mobile emulation.
    Returns configured WebDriver instance.
    """
    chrome_options = Options()

    # Configure mobile emulation
    mobile_emulation = {
        "deviceMetrics": {"width": 375, "height": 812, "pixelRatio": 3.0},
        "userAgent": "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0 Mobile/15E148 Safari/604.1"
    }
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)

    return driver

