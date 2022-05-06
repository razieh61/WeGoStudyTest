import datetime
from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import wegostudy_locators as locators
from selenium.webdriver.support.ui import Select


s = Service(executable_path='../chromedriver')
driver = webdriver.Chrome(service=s)


def setUp():
    print(f'Launch {locators.app} App')
    print(f'-------------------------***--------------------------')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.wegostudy_url)
    if driver.current_url == locators.wegostudy_url and driver.title == locators.wegostudy_home_page_title:
        print(f'Yey! {locators.app} website launched successfully')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch. check your code or application')
        print(f'Current URL: {driver.current_url}, Page title: {driver.title}')


def tearDown():
    if driver is not None:
        print(f'-------------------------***--------------------------')
        print(f'The test is completed at: {datetime.datetime.now()}')
        sleep(0.5)
        driver.close()
        driver.quit()


