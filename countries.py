import requests


country = input("Enter country name: \nDefault- India\n") or "india"
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
