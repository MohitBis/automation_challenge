import requests
import logging
logging.basicConfig(level = logging.INFO)

rancher_url = "http://x.x.x.x:8080/"
response = requests.get(rancher_url)

if response.status_code:
    logging.info("Pass: Login into Rancher")
    logging.info(response.json())
else:
    logging.error("Fail: Login into Rancher")

