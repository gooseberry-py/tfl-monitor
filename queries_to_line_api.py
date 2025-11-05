# created on 30/10/25 by gooseberry-py on a raspberry pi 5
import asyncio
import os
import httpx
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
    all_modes = await client.meta.modes.get()
    #rich.print(all_modes)

    # get tube lines
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    tube_lines = await client.mode.by_modes("tube").get()
    #rich.print(await client.mode.by_modes("tube").get())

    #Get all valid routes for all lines, including the name and id of the originating and terminating stops for each route.
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteSequenceByPathIdPathDirectionQueryServiceTypesQueryExcludeCrowding
    request_configuration = RequestConfiguration()
    request_configuration.headers = HeadersCollection()
    request_configuration.headers.add("Accept", "application/json")
    request_configuration.query_parameters = {"serviceTypes": "Regular"}
    all_lines_routes = await client.route.get(request_configuration=request_configuration)
    #rich.print(await client.route.get(request_configuration=request_configuration))

    #Gets the line status of for all lines for the given modes
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_StatusByModeByPathModesQueryDetailQuerySeverityLevel
    request_configuration = RequestConfiguration()
    request_configuration.headers = HeadersCollection()
    request_configuration.headers.add("Accept", "application/json")
    request_configuration.query_parameters = {"modes": "tube"}
    request_configuration.query_parameters = {"detail": True}
    all_tube_status = await client.mode.item.status.get(request_configuration=request_configuration)
    #todo find out how to get the status builder going
    all_tube_status = await client.mode.__init__()

    
    
    
    rich.print(all_tube_status)

    # can be an line so will try for bus 35 
    # inbound / outbound is the direction -- could be regular / night
    # rich.print(await client.route("northern","inbound","regular").get())


    #client.route.path_parameters["ids"] = "victoria"

    # todo figure out which query this actually is running









if __name__ == "__main__":
    asyncio.run(get_different_tfl_modes())
    #test_direct_request()