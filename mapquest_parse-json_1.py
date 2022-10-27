import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "New York, New York"
dest = "Los Angeles, California"
key = "RJ2gn0AMzZ8Q2Okaf2GQwetvvKLuyYrS"

url = main_api + urllib.parse.urlencode({"key":key, "from":orig, "to":dest})

json_data = requests.get(url).json()
print(json_data)
