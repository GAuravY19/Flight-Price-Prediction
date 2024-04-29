# ---------------------------------------------- Importing Libraries ---------------------------------------------------
import os
import time

import pandas as pd

from selenium import webdriver
from selenium.webdriver.edge.options import Options

from selenium.webdriver.common.action_chains import ActionChains

from utils.ShortMonth import Month_convert
from utils.Month_to_num import Month_converter_Num

# ----------------------------------------------------------------------------------------------------------------------

# --------------------------------------------- Initial Setup ----------------------------------------------------------

options = Options()
options.add_experimental_option("detach", True)

os.environ['PATH'] = 'D:/FlightsPricePrediction/WebScrapping/Webdriver/chromedriver.exe'

DRIVER = webdriver.Edge(options=options)

DRIVER.get('https://www.easemytrip.com/?msclkid=47862d64810f1926f8a24b4b9588c936')

DRIVER.maximize_window()

# ----------------------------------------------------------------------------------------------------------------------

# -------------------------------------------- Travel Information ------------------------------------------------------

FROM_CITY = "Mumbai"
DEST_CITY = "Delhi"

MONTH_NUM = Month_converter_Num('June')
DATE = 29
MONTH = Month_convert('June')
MONTH = MONTH.upper()
YEAR = 2024

ONE_WAY = True

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------- TRIP SELECTOR --------------------------------------------------
trip_type_selector = DRIVER.find_element('xpath', '//li[contains(@class, "activecl trip_type flig-show click-one") and contains(@id, "oway")]')
trip_type_selector.click()

from_box = DRIVER.find_element('xpath', "//p[text() = ' From']")
from_box.click()

from_box_enter = DRIVER.find_element('xpath', '//div/input[contains(@id, "a_FromSector_show") and contains(@placeholder,"From")]')
from_box_enter.send_keys(FROM_CITY)

time.sleep(2)

from_city_selection = DRIVER.find_element('xpath', f'//div/p/span[contains(text(), "{FROM_CITY}")]')
from_city_selection.click()

time.sleep(2)

dest_city_enter = DRIVER.find_element('xpath', '//div[contains(@class, "searcityCol")]//input[contains(@placeholder, "To")]')
dest_city_enter.send_keys(DEST_CITY)

time.sleep(2)

dest_city_selection = DRIVER.find_element('xpath', f'//div/p/span[contains(text(), "{DEST_CITY}")]')
dest_city_selection.click()

time.sleep(2)

# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------- Travel time selector -----------------------------------------------

travel_calendar_selection = DRIVER.find_element('xpath', f'//div[contains(@class, "month2")]')
present_month = travel_calendar_selection.text.split(" ")[0]

while(MONTH != present_month):
    next_mover = DRIVER.find_element('xpath', '''//div[contains(@class, "month3")]/img[contains(@onclick, "NextPrevClick('nxtMnt')")]''')
    next_mover.click()

    travel_calendar_selection = DRIVER.find_element('xpath', f'//div[contains(@class, "month2")]')
    present_month = travel_calendar_selection.text.split(" ")[0]

travel_date = DRIVER.find_element('xpath', f'//li/span[contains(@id, "{DATE}/{MONTH_NUM}/{YEAR}")]')
travel_date.click()

search_box = DRIVER.find_element('xpath', '//button[contains(@class, "srchBtnSe")]')
search_box.click()

# ----------------------------------------------------------------------------------------------------------------------

# scrolling the page

last_height = DRIVER.execute_script("return document.body.scrollHeight")

scroll_speed = 3

while True:
    DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    time.sleep(scroll_speed)

    new_height = DRIVER.execute_script("return document.body.scrollHeight")

    comapany_details = DRIVER.find_elements('xpath', '//div[contains(@class, "col-md-7 col-sm-7 padd-lft airl-txt-n")]/span[contains(@ng-bind, "GetAirLineName")]')
    departure_details = DRIVER.find_elements('xpath', '//div/span[contains(@ng-bind,"GetFltDtl(s.b[0].FL[0]).DTM")]')
    arival_details = DRIVER.find_elements('xpath', '//div/span[contains(@ng-bind,"GetFltDtl(s.b[0].FL[s.b[0].FL.length-1]).ATM")]')
    duration_detail = DRIVER.find_elements('xpath', '//div/span[contains(@class,"dura_md ng-binding") and contains(@ng-bind, "s.b[0].JyTm")]')
    not_stop_detail = DRIVER.find_elements('xpath', '//div/span[contains(@class,"dura_md2 ng-scope") and contains(@ng-if,"GetFltDtl")]')
    price_details = DRIVER.find_elements('xpath', '//div/span[contains(@ng-bind, "CurrencyDisplayRate(s.lstFr[0].TF+s.lstFr[0].FIA)")]')

    if new_height == last_height:
        break

    last_height = new_height

print(len(comapany_details))
print(len(departure_details))
print(len(arival_details))
print(len(duration_detail))
print(len(not_stop_detail))
print(len(price_details))

# ----------------------------------------------------------------------------------------------------------------------

# --------------------------------------- Getting flight details -------------------------------------------------------

COMPANY_NAME = []
DEPARTURE_TIME = []
ARRIVAL_TIME = []
DURATION = []
NON_STOP_OR_NOT = []
PRICE = []

for i in range(len(comapany_details)):
    COMPANY_NAME.append(comapany_details[i].text)
    DEPARTURE_TIME.append(departure_details[i].text)
    ARRIVAL_TIME.append(arival_details[i].text)
    DURATION.append(duration_detail[i].text)
    NON_STOP_OR_NOT.append(not_stop_detail[i].text)
    PRICE.append(price_details[i].text)

data = {
    'Company Name':COMPANY_NAME,
    'Departure Time':DEPARTURE_TIME,
    'Arrival Time':ARRIVAL_TIME,
    'Duration': DURATION,
    'Non stop': NON_STOP_OR_NOT,
    'Price':PRICE
}

df1 = pd.DataFrame(data, columns=['Company Name',
'Departure Time',
'Arrival Time',
'Duration',
'Non stop',
'Price'])

df1.to_csv('Dateformat.csv')

print("Safe zone reached bhai")
print(len(COMPANY_NAME))
print(len(DEPARTURE_TIME))


print("Kaam Hogaya")



















