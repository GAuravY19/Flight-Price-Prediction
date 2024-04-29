from setup import OneWayScrapper

if __name__ == "__main__":

    scrapper = OneWayScrapper()

    scrapper.initializer(from_city='Mumbai',
                        dest_city="Delhi",
                        date=29,
                        month='June',
                        year = 2024)

    scrapper.trip_type_selection(one_way=True)

    scrapper.From_info_enter()

    scrapper.To_city_enter()

    scrapper.travel_Date_input()

    scrapper.click_search()

    scrapper.collecting_data()

    scrapper.Making_csv_file()

    scrapper.saving_data()



    print("Kaam Hogaya")



















