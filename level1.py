from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
logging.basicConfig(level = logging.INFO)

driver = webdriver.Chrome(ChromeDriverManager().install())
# Test data
rancher_url = "http://x.x.x.x:8080/"
main_page_title = "Rancher"
logging.info("Test Data")
logging.info(f"Rancher dashboard url {rancher_url}")
logging.info(f"Expected main page title {main_page_title}")

# Login to Rancher webpage
logging.info(f"logging to rancher dashboard {rancher_url}")
driver.get(rancher_url)

# Check main web page title
result = driver.title
logging.info(f"title value {result}")
if result == main_page_title:
    logging.info(f"Pass : title value as expected {result}")
else:
    logging.error(f"Fail : tile value {result} not matching with expected value {expected_output} ")

# Close browser
driver.quit()