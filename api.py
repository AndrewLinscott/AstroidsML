#!/usr/bin/python

print("\n-------------------")

import pandas as pd
import requests
from requests import get
import json

response = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-04-29&end_date=2021-04-29&api_key=XZ7Oqn3CjkhXOUejPdNWxNXiaabdU9096yKXo2Qa")

print(response.status_code)

print(response.json())

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

jprint(response.json())

#nasaAstroids = pd.read_json("https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-04-29&end_date=2021-04-29&api_key=DEMO_KEY")
#nasaAstroids.info()

nasaAstroids = pd.read_json("https://api.nasa.gov/neo/rest/v1/feed?start_date=2021-04-29&end_date=2021-04-29&api_key=XZ7Oqn3CjkhXOUejPdNWxNXiaabdU9096yKXo2Qa")

#nasaAstroids=pd.json_normalize(nasaAstroids)
