from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import webdriver_manager.chrome
global driver

#pip3 install webdriver-manager
options = Options()
options.add_argument("start-maximized")
options.add_argument("--use-fake-ui-for-media-stream")
driver = webdriver.Chrome(service=Service(webdriver_manager.chrome.ChromeDriverManager().install()), options=options)
driver.get("https://involveprecan.involverh.com.mx")


