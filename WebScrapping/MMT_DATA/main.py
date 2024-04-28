import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

# Initial setup of driver
options = Options()
options.add_experimental_option("detach", True)

os.environ['PATH'] = 'D:/FlightsPricePrediction/WebScrapping/Webdriver/chromedriver.exe'

DRIVER = webdriver.Chrome(options=options)

DRIVER.get('https://www.makemytrip.com/')
DRIVER.maximize_window()

from_city = 'Mumbai'
destination_city = 'Bengaluru'

action = ActionChains(DRIVER)
action.move_by_offset(20, 190).click().perform()

time.sleep(5)

action = ActionChains(DRIVER)
action.move_by_offset(20, 190).click().perform()

time.sleep(2)

one_way_trip_selection = DRIVER.find_element('xpath', '//li[contains(@data-cy, "oneWayTrip")]')
one_way_trip_selection.click()

from_city_box_click = DRIVER.find_element('xpath', '//div/label[contains(@for, "fromCity")]')
from_city_box_click.click()

from_city_location_enter = DRIVER.find_element('xpath', '//input[contains(@placeholder,"From")]')
from_city_location_enter.send_keys(from_city)

time.sleep(2)

from_city_location = DRIVER.find_element('xpath', f'//div/p/span/span[contains(text(), "{from_city}")]')
from_city_location.click()

destination_city_box_click = DRIVER.find_element('xpath', '//div/label[contains(@for, "toCity")]')
destination_city_box_click.click()

destination_city_enter = DRIVER.find_element('xpath', '//input[contains(@placeholder, "To")]')
destination_city_enter.send_keys(destination_city)

time.sleep(2)

destination_city_location = DRIVER.find_element('xpath', f'//div/p/span/span[contains(text(), "{destination_city}")]')
destination_city_location.click()

print("Pura code run hogaya bhai.")
