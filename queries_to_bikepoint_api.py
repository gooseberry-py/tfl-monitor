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


async def get_all_borris_bike_info():
    #this works even without an API key
    #Gets all bike point locations. The Place object has an addtionalProperties array which contains the nbBikes, nbDocks and nbSpaces numbers which give the status of the BikePoint. A mismatch in these numbers i.e. nbDocks - (nbBikes + nbSpaces) != 0 indicates broken docks.
    #https://api-portal.tfl.gov.uk/api-details#api=BikePoint&operation=BikePoint_GetAll
    bb_info = requests.get(f"https://api.tfl.gov.uk/BikePoint/")
    bikepoint_json = json.loads(bb_info.text)
    return bikepoint_json


async def get_specific_borris_bike_info(dict_of_useful_bikepoints):
    #Gets the bike point with the given id.
    #https://api-portal.tfl.gov.uk/api-details#api=BikePoint&operation=BikePoint_Get
    bike_info_df = pd.DataFrame(columns=["id", "commonName", "NbBikes", "NbEmptyDocks", "NbDocks", "NbStandardBikes", "NbEBikes"])
    
    for id in dict_of_useful_bikepoints.keys():
        bikepoint_info_raw = requests.get(f"https://api.tfl.gov.uk/BikePoint/{id}")
        bikepoint_info = json.loads(bikepoint_info_raw.text)
        #info from the bikepoint
        new_row = {}
        new_row["id"] = bikepoint_info["id"]
        new_row["commonName"] = bikepoint_info["commonName"]
        for x in range(len(bikepoint_info["additionalProperties"])):
            if bikepoint_info["additionalProperties"][x]["key"] == "NbBikes":
                new_row["NbBikes"] = bikepoint_info["additionalProperties"][x]["value"]
            if bikepoint_info["additionalProperties"][x]["key"] == "NbEmptyDocks":
                new_row["NbEmptyDocks"] = bikepoint_info["additionalProperties"][x]["value"]
            if bikepoint_info["additionalProperties"][x]["key"] == "NbDocks":
                new_row["NbDocks"] = bikepoint_info["additionalProperties"][x]["value"]
            if bikepoint_info["additionalProperties"][x]["key"] == "NbStandardBikes":
                new_row["NbStandardBikes"] = bikepoint_info["additionalProperties"][x]["value"]
            if bikepoint_info["additionalProperties"][x]["key"] == "NbEBikes":
                new_row["NbEBikes"] = bikepoint_info["additionalProperties"][x]["value"]       
        bike_info_df.loc[len(bike_info_df)] = new_row
    return bike_info_df

if __name__ == "__main__":
    dict_of_useful_bikepoints = {
    "BikePoints_355":"Clapham Common Station, Clapham Common",
    "BikePoints_808":"Gauden Road, Clapham",
    "BikePoints_55":"Finsbury Circus, Liverpool Street",
    }
    
    bike_info = asyncio.run(get_specific_borris_bike_info(dict_of_useful_bikepoints))
    rich.print(bike_info)