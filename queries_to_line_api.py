# created on 30/10/25 by gooseberry-py on a raspberry pi 5
import asyncio
import os
import httpx
import pandas as pd
import json
import rich
import requests
from dotenv import load_dotenv
from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)

# from kiota_serialization.json.json_parse_node_factory import JsonParseNodeFactory
from kiota_abstractions.headers_collection import HeadersCollection
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import (
    JsonSerializationWriterFactory,
)

from tfl_api_line.tfl_api_line import Tfl_api_line
#how to get past the item problem
from tfl_api_line.item.stop_points.stop_points_request_builder import StopPointsRequestBuilder
from tfl_api_line.item.status.status_request_builder import StatusRequestBuilder


# load environment variables from .env file
load_dotenv(dotenv_path="config.env")


async def run_headers_and_api():
    # retrieve variables with defaults and type conversion
    api_key = os.getenv("TFL_API_KEY")

    # validate required variables
    if not api_key:
        raise ValueError(
            "TFL_API_KEY is required but not set in environment variables."
        )

    # header
    header = HeadersCollection()
    header.add("Accept", "application/json")

    # JSON parse factory
    parse_node_factory = JsonParseNodeFactory()
    serialization_writer_factory = JsonSerializationWriterFactory()

    # request adapter
    adapter = HttpxRequestAdapter(
        base_url="https://api.tfl.gov.uk",
        http_client=httpx.AsyncClient(verify=True),
        authentication_provider=ApiKeyAuthenticationProvider(
            key_location=KeyLocation.Header, api_key=api_key, parameter_name="x-api-key"
        ),
        serialization_writer_factory=serialization_writer_factory,
        parse_node_factory=parse_node_factory,
    )

    # API client
    client = Tfl_api_line(adapter)
    return client

async def _get_list_modes():
    # Gets a list of valid modes
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_MetaModes
    all_modes = requests.get(f'https://api.tfl.gov.uk/Line/Meta/Modes')
    return all_modes

async def _get_tube_lines(modes='tube'):
    # get tube lines
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    tube_lines = requests.get(f'https://api.tfl.gov.uk/Line/Mode/{modes}/Status')
    return tube_lines

async def _all_valid_routes_all_lines():
    #Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteByModeByPathModesQueryServiceTypes
    service_type = 'Regular' # or 'Night'
    modes = "tube"
    all_lines_routes = requests.get(f'https://api.tfl.gov.uk/Line/Mode/{modes}/Route?serviceTypes={service_type}')
    return all_lines_routes

async def _all_valid_routes_single_line(line):
    #Gets all valid routes for given line id, including the sequence of stops on each route.
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteSequenceByPathIdPathDirectionQueryServiceTypesQueryExcludeCrowding
    service_type = 'Regular' # or 'Night'
    all_routes_single = requests.get(f'https://api.tfl.gov.uk/Line/{line}/Route/Sequence/all?serviceTypes={service_type}')
    return all_routes_single
    
    

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
    modes = "tube" #"bus" "dlr" are valid
    status_dict = {}
    status_raw = requests.get(f"https://api.tfl.gov.uk/Line/Mode/{modes}/Status")
    status_neat = json.loads(status_raw.text)
    for x in range(len(status_neat)):
        id_key  = status_neat[x]["name"]
        id_body = status_neat[x]["lineStatuses"][0]["statusSeverityDescription"]
        status_dict[id_key] = id_body
    return status_dict

async def _train_or_bus_timetable(dict_of_useful_tube_and_bus_stops):
    #Gets the timetable for a specified station on the give line
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_TimetableByPathFromStopPointIdPathId
    tube_bus_schedule = {}
    for station, line in dict_of_useful_tube_and_bus_stops.values():
        schedule_raw = requests.get(f"https://api.tfl.gov.uk/Line/{line}/Timetable/{station}")
        schedule_neat = json.loads(schedule_raw.text)
        tube_bus_schedule[(line, schedule_neat[0]["stationName"])] = schedule_neat
    return tube_bus_schedule


async def _next_train_or_bus(dict_of_useful_tube_and_bus_stops):
    #Get the list of arrival predictions for given line ids based at the given stop
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_ArrivalsWithStopPointByPathIdsPathStopPointIdQueryDirectionQueryDestina
    next_transport_dict = {}
    for station, line in dict_of_useful_tube_and_bus_stops.values():
        schedule_raw = requests.get(f"https://api.tfl.gov.uk/Line/{line}/Arrivals/{station}")
        schedule_neat = json.loads(schedule_raw.text)
        station_and_direction = f'{schedule_neat[0]["stationName"]} {schedule_neat[0]["platformName"]}'
        next_transport_dict[(line, station_and_direction)] = schedule_neat
    return next_transport_dict

if __name__ == "__main__":
    client = asyncio.run(run_headers_and_api())
    #generic tube information functions
    list_of_modes = asyncio.run(_get_list_modes())
    list_of_tube_lines = asyncio.run(_get_tube_lines("northern"))
    routes_all_lines = asyncio.run(_all_valid_routes_all_lines())
    routes_single_line = asyncio.run(_all_valid_routes_single_line('northern'))
    tube_line_status = asyncio.run(_get_tube_status_update())
    
    lines_to_check = ["northern", "35", "37", "155"]
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
    tube_and_bus_timetable = asyncio.run(_train_or_bus_timetable(dict_of_useful_tube_and_bus_stops))
    next_tube_and_bus = asyncio.run(_next_train_or_bus(dict_of_useful_tube_and_bus_stops))


    print("stops")