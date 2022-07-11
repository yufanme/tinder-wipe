# todo 1 set the driver
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

CHROME_PATH = "/Users/fan/Development/chromedriver"
TINDER_URL = "https://tinder.com/"


service = Service(executable_path=CHROME_PATH)
driver = webdriver.Chrome(service=service)
driver.get(TINDER_URL)

# todo 2 loggin in the acount
# todo 3 click like for 100 times
# todo 4 quit the account and driver

