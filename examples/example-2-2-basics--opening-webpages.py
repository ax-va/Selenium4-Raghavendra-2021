import os
import pathlib
import sys
import time

# Get the package directory
package_dir = str(pathlib.Path(__file__).resolve().parents[1])
# Add the package directory into sys.path if necessary
if package_dir not in sys.path:
    sys.path.insert(0, package_dir)

# my modules
import utils.webdrivers as webdrivers


driver = webdrivers.get_chrome_webdriver()
# Open URL page
driver.get("https://github.com/ax-va/Selenium4-Raghavendra-2021")
time.sleep(5)
# Open FILE page
website_abspath = os.path.abspath("../websites/website/index.html")
driver.get("file:///" + website_abspath)
time.sleep(5)
driver.quit()