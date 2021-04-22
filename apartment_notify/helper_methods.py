import requests
import math
import smtplib
import json

from lxml import html
from typing import List

from apartment import Apartment

def __get_number_of_results(url):
    r = requests.get(url + "1")
    tree = html.fromstring(r.text)
    num_of_results = tree.xpath(".//div[@class='brojrezultata']/span")[0]
    return int(num_of_results.text)

def get_number_of_pages(url):
    num_of_results = __get_number_of_results(url)
    return math.ceil(num_of_results/30)

def get_current_apartments() -> List[Apartment]:
    current_apartments: List[Apartment] = []
    with open("urls.txt", 'r') as file:
        temp_list = file.read().splitlines()
    for elem in temp_list:
        url = elem.split(",")[0].strip()
        price = elem.split(",")[1].strip()
        current_apartments.append(Apartment(url, price))
    return current_apartments

def get_apartments(url) -> List[Apartment]:
    r = requests.get(url)
    tree = html.fromstring(r.text)
    apartments = tree.xpath(".//div[contains(@class,'imaHover')]")
    apartments_list: List[Apartment] = []
    for apartment in apartments:
        apartment_url: str = apartment.xpath(".//div[@class='naslov']/a")[0].attrib.get("href")
        price: str = apartment.xpath(".//div[@class='datum']/span[1]/text()[1]")[0].strip()
        apartments_list.append(Apartment(apartment_url, price))
    
    return apartments_list

def save_apartments(current_apartments: List[Apartment]):
    with open("urls.txt", "w") as file:
        file.write('\n'.join(f"{appartment.url}, {appartment.price}" for appartment in current_apartments))

def save_new_apartments(new_apartments: List[Apartment]):
    if len(new_apartments):
        with open("newUrls.txt", "w") as file:
            file.write("New: \n")
            file.write('\n'.join(f"{appartment.url}, {appartment.price}" for appartment in new_apartments))
            file.write("\n")

def save_deleted_apartments(deleted_apartments: List[Apartment]):
    if len(deleted_apartments):
        with open("deletedUrls.txt", "w") as file:
            file.write("Deleted:\n")
            file.write('\n'.join(f"{appartment.url}, {appartment.price}" for appartment in deleted_apartments))
            file.write("\n")

    files = ['newUrls.txt', 'deletedUrls.txt']
    bodyText = ''.join([open(f).read() for f in files])
    with open("body.txt", "w") as fo:
        fo.write(bodyText)
