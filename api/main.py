from typing import Union

from fastapi import FastAPI
import requests
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
from pydantic import BaseModel

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Zip(BaseModel):
    zip: str

url = "https://secure.shippingapis.com/ShippingAPI.dll?API=CityStateLookup"


@app.post("/find-zip")
async def get_city_state(zip:Zip):
    zip_dict = zip.dict()
    zip_value = zip_dict['zip']
    xml = f'<CityStateLookupRequest USERID="436TYREN7317"><ZipCode ID= "0"><Zip5>{zip_value}</Zip5></ZipCode></CityStateLookupRequest>'
    response = requests.get(f'{url}&xml={xml}')
    return response.content
