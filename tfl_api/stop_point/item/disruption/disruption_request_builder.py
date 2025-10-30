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
    from ....models.tfl.api.presentation.entities.disrupted_point import DisruptedPoint

class DisruptionRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/{ids-id}/Disruption
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new DisruptionRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/{ids%2Did}/Disruption{?flattenResponse*,getFamily*,includeRouteBlockedStops*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[DisruptionRequestBuilderGetQueryParameters]] = None) -> Optional[list[DisruptedPoint]]:
        """
        Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[DisruptedPoint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ....models.tfl.api.presentation.entities.disrupted_point import DisruptedPoint

        return await self.request_adapter.send_collection_async(request_info, DisruptedPoint, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[DisruptionRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> DisruptionRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: DisruptionRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return DisruptionRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class DisruptionRequestBuilderGetQueryParameters():
        """
        Gets all disruptions for the specified StopPointId, plus disruptions for any child Naptan records it may have.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "flatten_response":
                return "flattenResponse"
            if original_name == "get_family":
                return "getFamily"
            if original_name == "include_route_blocked_stops":
                return "includeRouteBlockedStops"
            return original_name
        
        # Specify true to associate all disruptions with parent stop point. (Only applicable when getFamily is true).
        flatten_response: Optional[bool] = None

        # Specify true to return disruptions for entire family, or false to return disruptions for just this stop point. Defaults to false.
        get_family: Optional[bool] = None

        include_route_blocked_stops: Optional[bool] = None

    
    @dataclass
    class DisruptionRequestBuilderGetRequestConfiguration(RequestConfiguration[DisruptionRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

