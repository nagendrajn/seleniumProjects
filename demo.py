import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.service import Service

driver = webdriver.Chrome()
driver.get("https://pypi.org/project/selenium/#files")
driver.maximize_window()
driver.find_element(By.XPATH, "//a[@id='history-tab']").click()
time.sleep(3)
driver.back()
driver.find_element(By.CSS_SELECTOR, "div[class='vertical-tabs__tabs'] a[class='vertical-tabs__tab "
                                     "vertical-tabs__tab--with-icon vertical-tabs__tab--condensed']").click()
time.sleep(3)
driver.close()
