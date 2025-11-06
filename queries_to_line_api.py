# created on 30/10/25 by gooseberry-py on a raspberry pi 5
import asyncio
import os
import httpx
import pandas as pd
import json
import rich
import requests

async def _get_list_modes():
    # Gets a list of valid modes
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_MetaModes
    all_modes = requests.get(f'https://api.tfl.gov.uk/Line/Meta/Modes')
    all_modes_clean = json.loads(all_modes.text)
    all_modes_list = []
    for item in range(len(all_modes_clean)):
        all_modes_list.append(all_modes_clean[item]["modeName"])
    return all_modes_list

async def _get_tube_lines(modes):
    # get tube lines
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    tube_lines = requests.get(f'https://api.tfl.gov.uk/Line/Mode/{modes}/Status')
    tube_lines_clean = json.loads(tube_lines.text)
    tube_lines_list = []
    for item in range(len(tube_lines_clean)):
        tube_lines_list.append(tube_lines_clean[item]["name"])
    return tube_lines_list

async def _all_valid_routes_all_lines(modes):
    #Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteByModeByPathModesQueryServiceTypes
    service_type = 'Regular' # or 'Night'
    all_lines_routes = requests.get(f'https://api.tfl.gov.uk/Line/Mode/{modes}/Route?serviceTypes={service_type}')
    all_lines_routes_clean = json.loads(all_lines_routes.text)
    return all_lines_routes_clean

async def _all_valid_routes_single_line(line):
    #Gets all valid routes for given line id, including the sequence of stops on each route.
    #We get the name, location, and IDs of different stops on the line
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteSequenceByPathIdPathDirectionQueryServiceTypesQueryExcludeCrowding
    service_type = 'Regular' # or 'Night'
    all_routes_single = requests.get(f'https://api.tfl.gov.uk/Line/{line}/Route/Sequence/all?serviceTypes={service_type}')
    all_routes_single_clean = json.loads(all_routes_single.text)   
    return all_routes_single_clean

async def _get_stops_on_a_line(lines_to_check):
    stops_dict = {}
    for transport in lines_to_check:
        stops_on_line = requests.get(f"https://api.tfl.gov.uk/Line/{transport}/StopPoints")
        rich.print(stops_on_line)
        stops_on_line_neat = json.loads(stops_on_line.text)
        stops = [{"id": item["naptanId"], "name":item["commonName"]} for item in stops_on_line_neat]
        stops_dict[transport] = stops
    return stops_dict

async def _get_tube_status_update():
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    modes = "tube" #"bus" "dlr" are valid - try 'national-rail'
    status_dict = {}
    status_raw = requests.get(f"https://api.tfl.gov.uk/Line/Mode/{modes}/Status")
    status_neat = json.loads(status_raw.text)
    for x in range(len(status_neat)):
        id_key  = status_neat[x]["name"]
        id_body = status_neat[x]["lineStatuses"][0]["statusSeverityDescription"]
        status_dict[id_key] = id_body
    return status_dict

async def _next_train_or_bus(dict_of_useful_tube_and_bus_stops):
    #Get the list of arrival predictions for given line ids based at the given stop
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_ArrivalsWithStopPointByPathIdsPathStopPointIdQueryDirectionQueryDestina
    next_transport_dict = {}
    eta_dashboard_cols = ['modeName', 'stationName', 'platformName', 'expectedArrival', 'currentLocation',]
    eta_dashboard_df = pd.DataFrame(columns=eta_dashboard_cols)
    for station, line in dict_of_useful_tube_and_bus_stops.values():
        schedule_raw = requests.get(f"https://api.tfl.gov.uk/Line/{line}/Arrivals/{station}")
        schedule_neat = json.loads(schedule_raw.text)
        station_and_direction = f'{schedule_neat[0]["stationName"]} {schedule_neat[0]["platformName"]}'
        next_transport_dict[(line, station_and_direction)] = schedule_neat
    for y in next_transport_dict.keys():
        for z in range(len(next_transport_dict[y])):
            new_row = {}
            new_row['modeName'] = next_transport_dict[y][z]["modeName"]
            new_row['stationName'] = next_transport_dict[y][z]["stationName"]
            if next_transport_dict[y][z]["modeName"] == "tube":
                new_row['platformName'] = next_transport_dict[y][z]["platformName"]
            elif next_transport_dict[y][z]["modeName"] == "bus":
                new_row['platformName'] = next_transport_dict[y][z]["lineName"]
            new_row['expectedArrival'] = next_transport_dict[y][z]["expectedArrival"]
            if next_transport_dict[y][z]["currentLocation"]:
                new_row['currentLocation'] = next_transport_dict[y][z]["currentLocation"]
            eta_dashboard_df.loc[len(eta_dashboard_df)] = new_row#platformName will also be lineName
    
    return eta_dashboard_df

if __name__ == "__main__":
    #generic tube information functions
    list_of_modes = asyncio.run(_get_list_modes())
    list_of_tube_lines = asyncio.run(_get_tube_lines("tube"))
    routes_all_lines = asyncio.run(_all_valid_routes_all_lines("tube"))
    routes_single_line = asyncio.run(_all_valid_routes_single_line('northern'))
    # in dashboard
    tube_line_status = asyncio.run(_get_tube_status_update())
    
    #more detailed checks for my needs that will get into the dashboard
    lines_to_check = ["northern", "35", "37", "155"]
    #this tells me which stops exist on different lines but will not be used in the dashboard
    stops = asyncio.run(_get_stops_on_a_line(lines_to_check))

    dict_of_useful_tube_and_bus_stops={
    "Clapham Common Underground Station":("940GZZLUCPC","northern"),
    'Clapham Common Station Bus 1':('490000050E',"35"),#northbound
    'Clapham Common Station Bus 2':('490000050K',"35"),#southbound to CJ
    'Clapham Common Station Bus 3':('490000050E',"37"),#northbound
    'Clapham Common Station Bus 4':('490000050K',"37"),#southbound to CJ
    'Clapham Common Station Bus 5':('490000050D',"155"),#northbound to Oval
    'Clapham Common Station Bus 6':('490000050G',"155"),#southbound
    'Oval Station Bus 1':('490000172Q',"155"),#northbound
    'Oval Station Bus 2':('490000172R',"155"),#southbound to CC
    }
    next_tube_and_bus = asyncio.run(_next_train_or_bus(dict_of_useful_tube_and_bus_stops))


    print("stops")