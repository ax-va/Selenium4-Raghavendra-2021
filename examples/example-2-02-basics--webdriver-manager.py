import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

GITHUB_URL = "https://github.com/ax-va/Web-Tests-Selenium4-Raghavendra-2021"
# WDM for webdriver manager
CHROMEDRIVER_WDM_CACHE_PATH = "../webdrivers/chromedriver-wdm-cache"
GECKODRIVER_WDM_CACHE_PATH = "../webdrivers/geckodriver-wdm-cache"
CACHE_VALID_RANGE = 30  # days

# Open web Chrome browser using webdriver
driver_chrome = webdriver.Chrome(
    service=Service(
        ChromeDriverManager(
            path=CHROMEDRIVER_WDM_CACHE_PATH,
            cache_valid_range=CACHE_VALID_RANGE
        ).install()
    )
)
# Add URL to open in browser
driver_chrome.get(GITHUB_URL)

# Open web Firefox browser using webdriver
driver_firefox = webdriver.Firefox(
    service=Service(
        GeckoDriverManager(
            path=GECKODRIVER_WDM_CACHE_PATH,
            cache_valid_range=CACHE_VALID_RANGE
        ).install()
    )
)
# Add URL to open in browser
driver_firefox.get(GITHUB_URL)

time.sleep(5)

# Terminate the process for the driver
driver_firefox.quit()
# Terminate the process for the driver
driver_chrome.quit()
