from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import xmltodict
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Zip(BaseModel):
    zip: str

@app.post("/find-zip")
async def get_city_state(zip:Zip):
    url = "https://secure.shippingapis.com/ShippingAPI.dll?API=CityStateLookup"
    zip_dict = zip.dict()
    zip_value = zip_dict['zip']
    xml = f'<CityStateLookupRequest USERID="436TYREN7317"><ZipCode ID= "0"><Zip5>{zip_value}</Zip5></ZipCode></CityStateLookupRequest>'
    response = requests.get(f'{url}&xml={xml}')
    if response.status_code == 200:
        responseDict = xmltodict.parse(response.content)
        city = responseDict['CityStateLookupResponse']['ZipCode']['City']
        state = responseDict['CityStateLookupResponse']['ZipCode']['State']
        formatted_response = {
            "city" : city,
            "state" : state
        }
        return formatted_response
    else:
        return "sorry there has been an error"
