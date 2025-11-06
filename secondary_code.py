# created on 30/10/25 by gooseberry-py on a raspberry pi 5
import asyncio
import os
import httpx
import rich
from dotenv import load_dotenv
from kiota_abstractions.authentication.api_key_authentication_provider import (
    ApiKeyAuthenticationProvider,
    KeyLocation,
)

# from kiota_serialization.json.json_parse_node_factory import JsonParseNodeFactory
from kiota_abstractions.headers_collection import HeadersCollection
from kiota_abstractions.request_configuration import RequestConfiguration
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
from kiota_serialization_json.json_parse_node_factory import JsonParseNodeFactory
from kiota_serialization_json.json_serialization_writer_factory import (
    JsonSerializationWriterFactory,
)

from tfl_api_line.tfl_api_line import Tfl_api_line

# load environment variables from .env file
load_dotenv(dotenv_path="config.env")


async def get_different_tfl_modes():
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

    # Gets a list of valid modes
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_MetaModes
    #all_modes = await client.meta.modes.get()
    #rich.print(all_modes)

    # get tube lines
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    #rich.print(await client.mode.by_modes("tube").get())

    # get all the stops on the northern line
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteSequenceByPathIdPathDirectionQueryServiceTypesQueryExcludeCrowding
    # can be an line so will try for bus 35 
    # inbound / outbound is the direction -- could be regular / night
    # rich.print(await client.route("northern","inbound","regular").get())
    request_configuration = RequestConfiguration()
    request_configuration.headers = HeadersCollection()
    request_configuration.headers.add("Accept", "application/json")
    request_configuration.query_parameters = {"serviceTypes": "Regular"}


    client.route.path_parameters["ids"] = "victoria"
    rich.print(await client.route.get(request_configuration=request_configuration))
    # todo figure out which query this actually is running



import requests



def test_direct_request():
    #this works even without an API key
    ids = "victoria"
    serviceTypes = "Regular"
    test = requests.get(f"https://api.tfl.gov.uk/Line/{ids}/Route?serviceTypes={serviceTypes}")
    print(test) 


def test_request_from_tfl_website():
    #this doesnt work even with the API key in headers, it gives 403 forbidden
    import urllib.request, json

    try:
        url = "https://api.tfl.gov.uk/Line/northern/Route/Sequence/inbound?serviceTypes=Regular"

        hdr ={
        # Request headers
        'Cache-Control': 'no-cache',
        'app_key': os.getenv("TFL_API_KEY"),
        }

        req = urllib.request.Request(url, headers=hdr)

        req.get_method = lambda: 'GET'
        response = urllib.request.urlopen(req)
        print(response.getcode())
        print(response.read())
    except Exception as e:
        print(e)






#these are functions that dont work
    #Gets the line status of for all lines for the given modes
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    '''request_configuration = RequestConfiguration()
    request_configuration.headers = HeadersCollection()
    request_configuration.headers.add("Accept", "application/json")
    request_configuration.query_parameters = {"modes": "tube"}
    request_configuration.query_parameters = {"detail": True}
    stop_point_client = StopPointsRequestBuilder(request_adapter=adapter, path_parameters=request_configuration)
    all_tube_status = await stop_point_client.get()'''
    

    #Get the stops on a given line
    #Gets a list of the stations that serve the given line id
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StopPointsByPathIdQueryTflOperatedNationalRailStationsOnly
    #https://api.tfl.gov.uk/Line/{id}/StopPoints[?tflOperatedNationalRailStationsOnly]
    '''request_configuration = RequestConfiguration()
    request_configuration.headers = HeadersCollection()
    request_configuration.headers.add("Accept", "application/json")
    request_configuration.query_parameters = {"id": "northern"}
    request_configuration.query_parameters = {"tflOperatedNationalRailStationsOnly": True}
    stop_point_client = StopPointsRequestBuilder(request_adapter=adapter, path_parameters={"id": "northern"})
    all_stops_on_line = await stop_point_client.get()
    # path = f'item/stop_points.'
    # all_stops_on_line = await client.path.get()
    # .mode.item.status.get(request_configuration=request_configuration)
    rich.print(all_stops_on_line)'''
    
    



def test_query():
    id = "northern"
    tflOperatedNationalRailStationsOnly = True
    test = requests.get(f"https://api.tfl.gov.uk/Line/{id}/StopPoints")
    #test = requests.get(f"https://api.tfl.gov.uk/Line/{id}/StopPoints?tflOperatedNationalRailStationsOnly={tflOperatedNationalRailStationsOnly}")
    rich.print(test)
    nice = pd.read_json(test.text)
    nice1 = json.loads(test.text)
    # can be an line so will try for bus 35 
    # inbound / outbound is the direction -- could be regular / night
    # rich.print(await client.route("northern","inbound","regular").get())
    #client.route.path_parameters["ids"] = "victoria"

    # todo figure out which query this actually is running



if __name__ == "__main__":
    asyncio.run(get_different_tfl_modes())
    #test_direct_request()