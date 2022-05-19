import json, requests, sys
from pprint import pprint
import os
import time


def weatherReport():
    APPID = "197ce0f21c79a51b7743b1b98107a747"
    location = input(
        "Usage: city_name, 2-letter_country_code\nExample- Jaipur,IN (Default) \n"
    ).split(",")

    location = ",".join(location) or "jaipur,IN"

    # location = "Jaipur,IN"

    # Download the JSON data from OpenWeatherMap.org's API.
    url = f"https://api.openweathermap.org/data/2.5/forecast/?q={location}&cnt=3&appid={APPID}"  # cnt = no. of days
    response = requests.get(url)

    if response.status_code != 200:
        print(response.status_code)

    # Uncomment to see the raw JSON text:
    # print(response.text)
    # pprint(response.json())

    w = response.json()

    print(f"Current weather in {location}")

    print()
    print("Weather Report:")
    print("----------------------------------")
    print(w["city"]["name"], w["city"]["country"], "\n")

    for i in w["list"]:
        print("Date/Time: ", i["dt_txt"])
        celcius = i["main"]["temp"] - 273.15  # temp in kelvin
        print(format(celcius, ".1f") + chr(176) + "C", end="\t")
        print(i["weather"][0]["description"])
        print()


def jokes():
    url = "https://v2.jokeapi.dev/joke/Any"
    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)

    if response.status_code != 200:
        print(response.status_code)
    data = response.json()

    if data["type"] == "twopart":
        print(data["setup"])
        print(data["delivery"])
    else:
        print(data["joke"])


def countries():
    country = input("Enter country name: \nDefault- India\n") or "bharat"
    # country = "india"

    url = f"https://restcountries.eu/rest/v2/name/{country}"  # keyword
    # url = f"https://restcountries.eu/rest/v2/name/{country}?fullText=true"  # full name

    payload = {}
    headers = {}

    # response = requests.get(url, headers=headers, data=payload)
    response = requests.request("GET", url, headers=headers, data=payload)
    if response.status_code != 200:
        print(response.status_code)

    # pprint(response.json())

    data = response.json()

    print(f"{country.capitalize()} Report:")
    print("----------------------------------")

    print()
    other_names = data[0]["altSpellings"]
    borders = data[0]["borders"]
    area = data[0]["area"]
    calling = data[0]["callingCodes"]
    capital = data[0]["capital"]
    native_name = data[0]["nativeName"]
    population = data[0]["population"]
    region = data[0]["region"]
    sub_region = data[0]["subregion"]
    time_zone = data[0]["timezones"]
    domain = data[0]["topLevelDomain"]
    flag = data[0]["flag"]

    print("Native Name:    ", native_name)
    print("Alternate Name: ", ", ".join(other_names))
    print()
    print("-- Geograpghy --")
    print("Borders :         ", ", ".join(borders) or "NA")
    print("region/sub-region:", f"{region}/{sub_region}")
    print("Capital:          ", capital)
    print("Area:             ", area)
    print("Population:       ", population)

    print()
    print("-- Currency --")
    for k, v in data[0]["currencies"][0].items():
        print(f"{k}:  {v}")

    print()
    print("-- Languages --")
    for i in data[0]["languages"]:
        print("Name:        ", i["name"])
        print("Native Name: ", i["nativeName"], "\n")

    print()
    print("-- other details --")
    print("Calling Code:     ", ", ".join(calling))
    print("Time Zone:        ", ", ".join(time_zone))
    print("Flag:              ", flag)
    print("top level domain: ", ", ".join(domain))
    print()


def displayMenu():
    print(
        """
    1. Country Details
    2. Weather Report
    3. Url Shortner
    4. Joke
    5: Exit
    """
    )


while True:
    os.system("cls")
    displayMenu()
    mapping = {1: countries, 2: weatherReport, 4: jokes, 5: "exit"}
    choice = int(input("what do you want to check?"))
    if choice == 5:
        sys.exit()
    mapping[choice]()
    time.sleep(5)
