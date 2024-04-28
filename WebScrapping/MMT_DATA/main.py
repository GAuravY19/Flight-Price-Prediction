import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from selenium.webdriver.common.action_chains import ActionChains

from utils.shortDay import Day_converter
from utils.ShortMonth import Month_convert

# ---------------------------------------- Initial setup of driver ---------------------------------------------
options = Options()
options.add_experimental_option("detach", True)

os.environ['PATH'] = 'D:/FlightsPricePrediction/WebScrapping/Webdriver/chromedriver.exe'

DRIVER = webdriver.Chrome(options=options)

DRIVER.get('https://www.makemytrip.com/')
DRIVER.maximize_window()
# --------------------------------------------------------------------------------------------------------------


# ---------------------------------------------- Information ---------------------------------------------------
from_city = 'Mumbai'
destination_city = 'Bengaluru'
Date = 29
Month = 'June'
day = Day_converter('Saturday')
Year = 2024
# --------------------------------------------------------------------------------------------------------------


# ---------------------------------------- Removing Dialogue Boxes ---------------------------------------------
action = ActionChains(DRIVER)
action.move_by_offset(20, 190).click().perform()

time.sleep(5)

action = ActionChains(DRIVER)
action.move_by_offset(20, 190).click().perform()

time.sleep(2)
# --------------------------------------------------------------------------------------------------------------


# ---------------------------------------- Setting the search box ----------------------------------------------
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
# ------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------ Dates Input Box ----------------------------------------------
time.sleep(2)

present_month_in_the_box = DRIVER.find_element('xpath', '//div[contains(@class, "DayPicker-Caption")]/div')
present_month = present_month_in_the_box.text.split(" ")[0]

while(present_month != Month):
    next_arrow = DRIVER.find_element('xpath', '//span[contains(@class, "DayPicker-NavButton--next")]')
    next_arrow.click()

    present_month_in_the_box = DRIVER.find_element('xpath', '//div[contains(@class, "DayPicker-Caption")]/div')
    present_month = present_month_in_the_box.text.split(" ")[0]

month = Month_convert(Month)

time.sleep(2)

dates_block_click = DRIVER.find_element('xpath', f'//div[contains(@class,"DayPicker-Day") and contains(@aria-label, "{day} {month} {Date} {Year}")]')
dates_block_click.click()



print("Pura code run hogaya bhai.")
