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
    from .....models.tfl.api.presentation.entities.stop_point import StopPoint
    from .get_service_types_query_parameter_type import GetServiceTypesQueryParameterType

class WithLineItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/{ids-id}/CanReachOnLine/{lineId}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithLineItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/{ids%2Did}/CanReachOnLine/{lineId}{?serviceTypes*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithLineItemRequestBuilderGetQueryParameters]] = None) -> Optional[list[StopPoint]]:
        """
        Gets Stopoints that are reachable from a station/line combination.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[StopPoint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .....models.tfl.api.presentation.entities.stop_point import StopPoint

        return await self.request_adapter.send_collection_async(request_info, StopPoint, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithLineItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets Stopoints that are reachable from a station/line combination.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithLineItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithLineItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithLineItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithLineItemRequestBuilderGetQueryParameters():
        """
        Gets Stopoints that are reachable from a station/line combination.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "service_types":
                return "serviceTypes"
            return original_name
        
        # A comma-separated list of service types to filter on. If not specified. Supported values: Regular, Night. Defaulted to 'Regular' if not specified
        service_types: list[GetServiceTypesQueryParameterType] = field(default_factory=list)

    
    @dataclass
    class WithLineItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithLineItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

