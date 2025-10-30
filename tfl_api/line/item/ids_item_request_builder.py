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
    from ...models.tfl.api.presentation.entities.line import Line
    from .arrivals.arrivals_request_builder import ArrivalsRequestBuilder
    from .disruption.disruption_request_builder import DisruptionRequestBuilder
    from .route.route_request_builder import RouteRequestBuilder
    from .status.status_request_builder import StatusRequestBuilder
    from .stop_points.stop_points_request_builder import StopPointsRequestBuilder
    from .timetable.timetable_request_builder import TimetableRequestBuilder

class IdsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Line/{ids-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IdsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Line/{ids%2Did}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> Optional[list[Line]]:
        """
        Gets lines that match the specified line ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[Line]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.tfl.api.presentation.entities.line import Line

        return await self.request_adapter.send_collection_async(request_info, Line, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[QueryParameters]] = None) -> RequestInformation:
        """
        Gets lines that match the specified line ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> IdsItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: IdsItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return IdsItemRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def arrivals(self) -> ArrivalsRequestBuilder:
        """
        The Arrivals property
        """
        from .arrivals.arrivals_request_builder import ArrivalsRequestBuilder

        return ArrivalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disruption(self) -> DisruptionRequestBuilder:
        """
        The Disruption property
        """
        from .disruption.disruption_request_builder import DisruptionRequestBuilder

        return DisruptionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def route(self) -> RouteRequestBuilder:
        """
        The Route property
        """
        from .route.route_request_builder import RouteRequestBuilder

        return RouteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def status(self) -> StatusRequestBuilder:
        """
        The Status property
        """
        from .status.status_request_builder import StatusRequestBuilder

        return StatusRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop_points(self) -> StopPointsRequestBuilder:
        """
        The StopPoints property
        """
        from .stop_points.stop_points_request_builder import StopPointsRequestBuilder

        return StopPointsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def timetable(self) -> TimetableRequestBuilder:
        """
        The Timetable property
        """
        from .timetable.timetable_request_builder import TimetableRequestBuilder

        return TimetableRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[QueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

