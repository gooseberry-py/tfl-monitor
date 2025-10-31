# created on 30/10/25 by gooseberry-py on a raspberry pi 5
import os
from dotenv import load_dotenv
import asyncio
import httpx
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_http.httpx_request_adapter import HttpxRequestAdapter
#from kiota_serialization.json.json_parse_node_factory import JsonParseNodeFactory
from tfl_api.line.line_request_builder import LineRequestBuilder
from tfl_api.line.meta.modes.modes_request_builder import ModesRequestBuilder
from kiota_abstractions.headers_collection import HeadersCollection
from kiota_abstractions.authentication.authentication_provider import AuthenticationProvider


#load environment variables from .env file
load_dotenv(dotenv_path="config.env")

#retrieve variables with defaults and type conversion
api_key = os.getenv("tfl_api_key")
api_username = os.getenv("tfl_api_name")


#validate required variables
if not api_key:
    raise ValueError("TFL_API_KEY is required but not set in environment variables.")


header = HeadersCollection()
header.try_add("x-api-key", api_key)
authenticator_provider = AuthenticationProvider()
authenticator_provider.additional_authentication_context(header)



client = ModesRequestBuilder(
    request_adapter=HttpxRequestAdapter(
        http_client=httpx.AsyncClient(),
        authentication_provider=authenticator_provider,
        #parse_node_factory=JsonParseNodeFactory()
    ),
    path_parameters={}  
)

async def get_different_tfl_modes(api_key: str):
    #Gets a list of valid modes
    all_modes = await client.get(
        request_configuration=RequestConfiguration(
            query_parameters=QueryParameters(
                # Add any query parameters if needed
            ),
            headers=header
            
        )
    )
    

    print(all_modes)



# if __name__ == "__main__":
#     get_different_tfl_modes()


asyncio.run(get_different_tfl_modes(api_key=api_key))
