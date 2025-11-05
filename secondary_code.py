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
    #rich.print(await client.mode.by_modes("tube").get())

    # get all the stops on the northern line
    #https://api-portal.tfl.gov.uk/api-details#api=Line&operation=Line_RouteSequenceByPathIdPathDirectionQueryServiceTypesQueryExcludeCrowding
    # can be an line so will try for bus 35 
    # inbound / outbound is the direction -- could be regular / night
    # rich.print(await client.route("northern","inbound","regular").get())
    request_configuration = {'headers': header,
                            'service_types':"regular"}   


    client.route.path_parameters["ids"] = "Victoria"
    rich.print(await client.route.get(request_configuration=request_configuration))
    # todo figure out which query this actually is running


    import requests

    ids = "victoria"
    serviceTypes = "Regular"
    requests.get(f"https://api.tfl.gov.uk/Line/{ids}/Route?serviceTypes={service_type}")
    


if __name__ == "__main__":
    asyncio.run(get_different_tfl_modes())
