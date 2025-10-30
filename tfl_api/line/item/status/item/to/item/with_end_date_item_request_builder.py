from __future__ import annotations
import datetime
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
    from .......models.tfl.api.presentation.entities.line import Line

class WithEndDateItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Line/{ids-id}/Status/{StartDate}/to/{EndDate}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithEndDateItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Line/{ids%2Did}/Status/{StartDate}/to/{EndDate}?endDate={endDate}&startDate={startDate}{&dateRange%2EendDate*,dateRange%2EstartDate*,detail*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithEndDateItemRequestBuilderGetQueryParameters]] = None) -> Optional[list[Line]]:
        """
        Gets the line status for given line ids during the provided dates e.g Minor Delays
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Line]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .......models.tfl.api.presentation.entities.line import Line

        return await self.request_adapter.send_collection_async(request_info, Line, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithEndDateItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets the line status for given line ids during the provided dates e.g Minor Delays
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithEndDateItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithEndDateItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithEndDateItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithEndDateItemRequestBuilderGetQueryParameters():
        """
        Gets the line status for given line ids during the provided dates e.g Minor Delays
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "date_range_end_date":
                return "dateRange%2EendDate"
            if original_name == "date_range_start_date":
                return "dateRange%2EstartDate"
            if original_name == "end_date":
                return "endDate"
            if original_name == "start_date":
                return "startDate"
            if original_name == "detail":
                return "detail"
            return original_name
        
        date_range_end_date: Optional[datetime.datetime] = None

        date_range_start_date: Optional[datetime.datetime] = None

        # Include details of the disruptions that are causing the line status including the affected stops and routes
        detail: Optional[bool] = None

        end_date: Optional[str] = None

        start_date: Optional[str] = None

    
    @dataclass
    class WithEndDateItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithEndDateItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

