from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.base_request_configuration import RequestConfiguration
from kiota_abstractions.default_query_parameters import QueryParameters
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Optional, TYPE_CHECKING, Union
from warnings import warn

if TYPE_CHECKING:
    from ......models.system.object import Object

class WithLonItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Place/{-id}/At/{Lat}/{Lon}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLonItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Place/{%2Did}/At/{Lat}/{Lon}?lat={lat}&location.lat={location%2Elat}&location.lon={location%2Elon}&lon={lon}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithLonItemRequestBuilderGetQueryParameters]] = None) -> Optional[object]:
        """
        Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place            must be polygonal e.g. a BoroughBoundary.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[object]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.system.object import Object

        return await self.request_adapter.send_async(request_info, object, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithLonItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place            must be polygonal e.g. a BoroughBoundary.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithLonItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithLonItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithLonItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithLonItemRequestBuilderGetQueryParameters():
        """
        Gets any places of the given type whose geography intersects the given latitude and longitude. In practice this means the Place            must be polygonal e.g. a BoroughBoundary.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "location_lat":
                return "location%2Elat"
            if original_name == "location_lon":
                return "location%2Elon"
            if original_name == "lat":
                return "lat"
            if original_name == "lon":
                return "lon"
            return original_name
        
        lat: Optional[str] = None

        location_lat: Optional[float] = None

        location_lon: Optional[float] = None

        lon: Optional[str] = None

    
    @dataclass
    class WithLonItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithLonItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

