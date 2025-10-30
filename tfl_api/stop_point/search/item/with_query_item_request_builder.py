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
    from ....models.tfl.api.presentation.entities.search_response import SearchResponse

class WithQueryItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/Search/{query}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithQueryItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/Search/{query}{?faresOnly*,includeHubs*,lines*,maxResults*,modes*,tflOperatedNationalRailStationsOnly*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithQueryItemRequestBuilderGetQueryParameters]] = None) -> Optional[SearchResponse]:
        """
        Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[SearchResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.tfl.api.presentation.entities.search_response import SearchResponse

        return await self.request_adapter.send_async(request_info, SearchResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithQueryItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithQueryItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithQueryItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithQueryItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithQueryItemRequestBuilderGetQueryParameters():
        """
        Search StopPoints by their common name, or their 5-digit Countdown Bus Stop Code.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "fares_only":
                return "faresOnly"
            if original_name == "include_hubs":
                return "includeHubs"
            if original_name == "max_results":
                return "maxResults"
            if original_name == "tfl_operated_national_rail_stations_only":
                return "tflOperatedNationalRailStationsOnly"
            if original_name == "lines":
                return "lines"
            if original_name == "modes":
                return "modes"
            return original_name
        
        # True to only return stations in that have Fares data available for single fares to another station.
        fares_only: Optional[bool] = None

        # If true, returns results including HUBs.
        include_hubs: Optional[bool] = None

        # An optional, parameter separated list of the lines to filter by
        lines: Optional[list[str]] = None

        # An optional result limit, defaulting to and with a maximum of 50. Since children of the stop point heirarchy are returned for matches,            it is possible that the flattened result set will contain more than 50 items.
        max_results: Optional[int] = None

        # An optional, parameter separated list of the modes to filter by
        modes: Optional[list[str]] = None

        # If the national-rail mode is included, this flag will filter the national rail stations so that only those operated by TfL are returned
        tfl_operated_national_rail_stations_only: Optional[bool] = None

    
    @dataclass
    class WithQueryItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithQueryItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

