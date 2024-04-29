import os
import time

import pandas as pd

from selenium import webdriver
from selenium.webdriver.edge.options import Options

from selenium.webdriver.common.action_chains import ActionChains

from utils.ShortMonth import Month_convert
from utils.Month_to_num import Month_converter_Num


class OneWayScrapper:

    def __init__(self):
        self.options = Options()
        self.options.add_experimental_option("detach", True)

        os.environ['PATH'] = 'D:/FlightsPricePrediction/WebScrapping/Webdriver/chromedriver.exe'

        self.DRIVER = webdriver.Edge(options=self.options)

        self.DRIVER.get("https://www.easemytrip.com/?msclkid=47862d64810f1926f8a24b4b9588c936")

        self.DRIVER.maximize_window()

        self.COMPANY_NAME = []
        self.DEPARTURE_TIME = []
        self.ARRIVAL_TIME = []
        self.DURATION = []
        self.NON_STOP_OR_NOT = []
        self.PRICE = []

        self.save_location_file = 'D:/FlightsPricePrediction/data/raw_data/Dateformat.csv'


    def initializer(self,from_city:str,
                    dest_city:str,
                    date:int,
                    month:str,
                    year) -> None:

        self.from_city = from_city

        self.dest_city = dest_city

        self.month_num = Month_converter_Num(month)

        self.date = date

        self.month = Month_convert(month)
        self.month = self.month.upper()

        self.year = 2024


    def trip_type_selection(self, one_way:bool) -> None:

        if one_way:
            trip_type_selector = self.DRIVER.find_element('xpath', '//li[contains(@class, "activecl trip_type flig-show click-one") and contains(@id, "oway")]')
            trip_type_selector.click()


    def From_info_enter(self):
        from_box = self.DRIVER.find_element('xpath', "//p[text() = ' From']")
        from_box.click()

        time.sleep(2)

        from_box_enter = self.DRIVER.find_element('xpath', '//div/input[contains(@id, "a_FromSector_show") and contains(@placeholder,"From")]')
        from_box_enter.send_keys(self.from_city)

        time.sleep(2)

        from_city_selection = self.DRIVER.find_element('xpath', f'//div/p/span[contains(text(), "{self.from_city}")]')
        from_city_selection.click()


    def To_city_enter(self):
        time.sleep(2)

        dest_city_enter = self.DRIVER.find_element('xpath', '//div[contains(@class, "searcityCol")]//input[contains(@placeholder, "To")]')
        dest_city_enter.send_keys(self.dest_city)

        time.sleep(2)

        dest_city_selection = self.DRIVER.find_element('xpath', f'//div/p/span[contains(text(), "{self.dest_city}")]')
        dest_city_selection.click()

        time.sleep(2)


    def travel_Date_input(self):
        travel_calendar_selection = self.DRIVER.find_element('xpath', f'//div[contains(@class, "month2")]')
        present_month = travel_calendar_selection.text.split(" ")[0]

        while(self.month != present_month):
            next_mover = self.DRIVER.find_element('xpath', '''//div[contains(@class, "month3")]/img[contains(@onclick, "NextPrevClick('nxtMnt')")]''')
            next_mover.click()

            travel_calendar_selection = self.DRIVER.find_element('xpath', f'//div[contains(@class, "month2")]')
            present_month = travel_calendar_selection.text.split(" ")[0]

        travel_date = self.DRIVER.find_element('xpath', f'//li/span[contains(@id, "{self.date}/{self.month_num}/{self.year}")]')
        travel_date.click()


    def click_search(self):
        search_box = self.DRIVER.find_element('xpath', '//button[contains(@class, "srchBtnSe")]')
        search_box.click()


    def collecting_data(self):

        time.sleep(7)

        last_height = self.DRIVER.execute_script("return document.body.scrollHeight")

        scroll_speed = 3

        while True:
            self.DRIVER.execute_script("window.scrollTo(0, document.body.scrollHeight)")

            time.sleep(scroll_speed)

            new_height = self.DRIVER.execute_script("return document.body.scrollHeight")

            comapany_details = self.DRIVER.find_elements('xpath', '//div[contains(@class, "col-md-7 col-sm-7 padd-lft airl-txt-n")]/span[contains(@ng-bind, "GetAirLineName")]')
            departure_details = self.DRIVER.find_elements('xpath', '//div/span[contains(@ng-bind,"GetFltDtl(s.b[0].FL[0]).DTM")]')
            arival_details = self.DRIVER.find_elements('xpath', '//div/span[contains(@ng-bind,"GetFltDtl(s.b[0].FL[s.b[0].FL.length-1]).ATM")]')
            duration_detail = self.DRIVER.find_elements('xpath', '//div/span[contains(@class,"dura_md ng-binding") and contains(@ng-bind, "s.b[0].JyTm")]')
            not_stop_detail = self.DRIVER.find_elements('xpath', '//div/span[contains(@class,"dura_md2 ng-scope") and contains(@ng-if,"GetFltDtl")]')
            price_details = self.DRIVER.find_elements('xpath', '//div/span[contains(@ng-bind, "CurrencyDisplayRate(s.lstFr[0].TF+s.lstFr[0].FIA)")]')

            if new_height == last_height:
                break

            last_height = new_height

        for i in range(len(comapany_details)):
            self.COMPANY_NAME.append(comapany_details[i].text)
            self.DEPARTURE_TIME.append(departure_details[i].text)
            self.ARRIVAL_TIME.append(arival_details[i].text)
            self.DURATION.append(duration_detail[i].text)
            self.NON_STOP_OR_NOT.append(not_stop_detail[i].text)
            self.PRICE.append(price_details[i].text)


    def Making_csv_file(self):

        data = {
            'Company Name':self.COMPANY_NAME,
            'Departure Time':self.DEPARTURE_TIME,
            'Arrival Time':self.ARRIVAL_TIME,
            'Duration': self.DURATION,
            'Non stop': self.NON_STOP_OR_NOT,
            'Price':self.PRICE
        }

        self.df1 = pd.DataFrame(data, columns=['Company Name',
                                            'Departure Time',
                                            'Arrival Time',
                                            'Duration',
                                            'Non stop',
                                            'Price'])


    def saving_data(self):
        self.df1.to_csv(self.save_location_file)
















