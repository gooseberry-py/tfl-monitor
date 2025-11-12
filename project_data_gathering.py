# created on 06/11/25 by gooseberry-py on a raspberry pi 5
import asyncio
import os
import httpx
import pandas as pd
import json
import rich
import requests
import time

from queries_to_bikepoint_api import get_all_borris_bike_info, get_specific_borris_bike_info
from queries_to_line_api import _get_list_modes, _get_tube_lines, _all_valid_routes_all_lines, _all_valid_routes_single_line, _get_tube_status_update, _get_stops_on_a_line, _next_train_or_bus


async def constant_data_pull():

    data_dict = {}
    tube_line_status = await _get_tube_status_update()
    tube_line_status1 = pd.DataFrame.from_dict(tube_line_status, orient='index', columns=['Status'])
    tube_line_status1.reset_index(inplace=True)
    tube_line_status1.rename(columns={'index':'Line'}, inplace=True)
    data_dict["tube_line_status"] = tube_line_status1

    dict_of_useful_tube_and_bus_stops={
    "Clapham Common Underground Station":("940GZZLUCPC","northern"),
    'Clapham Common Station Bus 2':('490000050K',"35"),#southbound to CJ
    'Clapham Common Station Bus 4':('490000050K',"37"),#southbound to CJ
    'Clapham Common Station Bus 5':('490000050D',"155"),#northbound to Oval
    'Dorset Road Oval 1':("490006134S", "155"),#southbound to CC - dorset road stop H
    }
    next_tube_and_bus_df = await _next_train_or_bus(dict_of_useful_tube_and_bus_stops)
    data_dict["next_tube_and_bus_df"] = next_tube_and_bus_df

    dict_of_useful_bikepoints = {
    "BikePoints_355":"Clapham Common Station, Clapham Common",
    "BikePoints_808":"Gauden Road, Clapham",
    "BikePoints_55":"Finsbury Circus, Liverpool Street",
    "BikePoints_603":"Caldwell Street, Stockwell"
    }
    borris_bike_df = await get_specific_borris_bike_info(dict_of_useful_bikepoints)
    data_dict["borris_bike_df"] = borris_bike_df
    return data_dict


if __name__ == "__main__":
    data_dict = asyncio.run(constant_data_pull())
    # while True:
    #     data_dict = asyncio.run(constant_data_pull())
    #     rich.print(data_dict)
    #     time.sleep(5) #runs every 5 seconds

