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

from tfl_api_swagger.tfl_api import Tfl_api

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
    client = Tfl_api(adapter)

    # Gets a list of valid modes
    all_modes = await client.line.meta.modes.get()
    rich.print(all_modes)

    # get tube lines
    rich.print(await client.line.mode.by_modes("tube").get())


if __name__ == "__main__":
    asyncio.run(get_different_tfl_modes())
