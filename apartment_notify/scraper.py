import requests
import helper_methods
import smtplib
import os
import json
from lxml import html
from apartment import Apartment
from typing import List

url = "https://www.olx.ba/pretraga?vrsta=samoprodaja&kategorija=23&sort_order=desc&kanton=9&grad%5B0%5D=3969&do=100000&kvadrata_min=40&kvadrata_max=55";

def main():
    current_apartments: List[Apartment] = helper_methods.get_current_apartments()
    new_apartments: List[Apartment] = []

    number_of_pages = helper_methods.get_number_of_pages(url)

    for i in range(helper_methods.get_number_of_pages(url)):
        new_apartments.extend(helper_methods.get_apartments(url + str(i + 1)))

    deleted_apartments_to_mail = []
    new_apartments_to_mail = []
    changed_apartments_prices_to_email = []
    
    temp_list = current_apartments.copy()
    for current_apartment in temp_list:
        for new_apartment in new_apartments:
            if current_apartment == new_apartment:
                if  current_apartment.price != new_apartment.price:
                    changed_apartments_prices_to_email.append(new_apartment)
                    current_apartments.remove(current_apartment)
                    current_apartments.append(new_apartment)

    temp_list = current_apartments.copy()
    for current_apartment in temp_list:
        if current_apartment not in new_apartments:
            deleted_apartments_to_mail.append(current_apartment)
            current_apartments.remove(current_apartment)

    for new_apartment in new_apartments:
        if new_apartment not in current_apartments:
            new_apartments_to_mail.append(new_apartment)
            current_apartments.append(new_apartment)

    helper_methods.save_apartments(current_apartments)
    helper_methods.save_new_apartments(new_apartments_to_mail)
    helper_methods.save_deleted_apartments(deleted_apartments_to_mail)

if __name__ == '__main__':
    main()
