from setup import OneWayScrapper

FROM_CITY = 'Mumbai'
DEST_CITY = 'Delhi'
DATE = 29
MONTH = 'June'
YEAR = 2024

if __name__ == "__main__":

    scrapper = OneWayScrapper()

    scrapper.initializer(from_city=FROM_CITY,
                        dest_city=DEST_CITY,
                        date=DATE,
                        month=MONTH,
                        year = YEAR)

    scrapper.trip_type_selection(one_way=True)

    scrapper.From_info_enter()

    scrapper.To_city_enter()

    scrapper.travel_Date_input()

    scrapper.click_search()

    scrapper.collecting_data()

    scrapper.Making_csv_file()

    scrapper.saving_data(f'{DATE}_{MONTH}_{YEAR}.csv')

    print("Kaam Hogaya")



















