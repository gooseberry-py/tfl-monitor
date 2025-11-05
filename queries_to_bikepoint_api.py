# created on 30/10/25 by gooseberry-py on a raspberry pi 5
import asyncio
import os
import httpx
import rich
from dotenv import load_dotenv
import requests
import pandas as pd
import json

# load environment variables from .env file
load_dotenv(dotenv_path="config.env")


def get_all_borris_bike_info():
    #this works even without an API key
    #Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0 indicates broken docks.
    #https://api-portal.tfl.gov.uk/api-details#api=BikePoint&operation=BikePoint_GetAll
    bb_info = requests.get(f"https://api.tfl.gov.uk/BikePoint/")
    bikepoint_test = json.loads(bb_info.text)
    #todo convert this into something useful


def get_specific_borris_bike_info():
    #this works even without an API key
    #Gets the bike point with the given id.
    # it doesnt tell me how many bikes are in the station so cant really see a use for it
    dict_of_useful_bikepoints{
        "BikePoints_355":"Clapham Common Station, Clapham Common",
        "BikePoints_808":"Gauden Road, Clapham",
        "BikePoints_55":"Finsbury Circus, Liverpool Street",
        }
    
    
    id = "BikePoints_355"
    #https://api-portal.tfl.gov.uk/api-details#api=BikePoint&operation=BikePoint_Get
    bb_info = requests.get(f"https://api.tfl.gov.uk/BikePoint/{id}")
    breakpoint()
    bikepoint_dataFrame = pd.read_json(bb_info.text)



if __name__ == "__main__":
    get_all_borris_bike_info()