from typing import Union

from fastapi import FastAPI
import requests

app = FastAPI()

url = "https://secure.shippingapis.com/ShippingAPI.dll?API=CityStateLookup"

@app.get("/find-zip")
def get_city_state(xml: str):
    response = requests.get(f'{url}&xml={xml}')
    return response
