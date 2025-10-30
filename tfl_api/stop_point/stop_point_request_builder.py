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
    from ..models.tfl.api.presentation.entities.stop_points_response import StopPointsResponse
    from .item.ids_item_request_builder import IdsItemRequestBuilder
    from .meta.meta_request_builder import MetaRequestBuilder
    from .mode.mode_request_builder import ModeRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .service_types.service_types_request_builder import ServiceTypesRequestBuilder
    from .sms.sms_request_builder import SmsRequestBuilder
    from .type.type_request_builder import TypeRequestBuilder

class StopPointRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new StopPointRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint?location.lat={location%2Elat}&location.lon={location%2Elon}&stopTypes={stopTypes}{&categories*,modes*,radius*,returnLines*,useStopPointHierarchy*}", path_parameters)
    
    def by_ids_id(self,ids_id: str) -> IdsItemRequestBuilder:
        """
        Gets an item from the tfl_api.StopPoint.item collection
        param ids_id: A comma-separated list of stop point ids (station naptan code e.g. 940GZZLUASL). Max. approx. 20 ids.            You can use /StopPoint/Search/{query} endpoint to find a stop point id from a station name.
        Returns: IdsItemRequestBuilder
        """
        if ids_id is None:
            raise TypeError("ids_id cannot be null.")
        from .item.ids_item_request_builder import IdsItemRequestBuilder

        url_tpl_params = get_path_parameters(self.path_parameters)
        url_tpl_params["ids%2Did"] = ids_id
        return IdsItemRequestBuilder(self.request_adapter, url_tpl_params)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[StopPointRequestBuilderGetQueryParameters]] = None) -> Optional[StopPointsResponse]:
        """
        Gets a list of StopPoints within {radius} by the specified criteria
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[StopPointsResponse]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ..models.tfl.api.presentation.entities.stop_points_response import StopPointsResponse

        return await self.request_adapter.send_async(request_info, StopPointsResponse, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[StopPointRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of StopPoints within {radius} by the specified criteria
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> StopPointRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: StopPointRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return StopPointRequestBuilder(self.request_adapter, raw_url)
    
    @property
    def meta(self) -> MetaRequestBuilder:
        """
        The Meta property
        """
        from .meta.meta_request_builder import MetaRequestBuilder

        return MetaRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mode(self) -> ModeRequestBuilder:
        """
        The Mode property
        """
        from .mode.mode_request_builder import ModeRequestBuilder

        return ModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The Search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def service_types(self) -> ServiceTypesRequestBuilder:
        """
        The ServiceTypes property
        """
        from .service_types.service_types_request_builder import ServiceTypesRequestBuilder

        return ServiceTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def sms(self) -> SmsRequestBuilder:
        """
        The Sms property
        """
        from .sms.sms_request_builder import SmsRequestBuilder

        return SmsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def type(self) -> TypeRequestBuilder:
        """
        The Type property
        """
        from .type.type_request_builder import TypeRequestBuilder

        return TypeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class StopPointRequestBuilderGetQueryParameters():
        """
        Gets a list of StopPoints within {radius} by the specified criteria
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
            if original_name == "return_lines":
                return "returnLines"
            if original_name == "stop_types":
                return "stopTypes"
            if original_name == "use_stop_point_hierarchy":
                return "useStopPointHierarchy"
            if original_name == "categories":
                return "categories"
            if original_name == "modes":
                return "modes"
            if original_name == "radius":
                return "radius"
            return original_name
        
        # an optional list of comma separated property categories to return in the StopPoint's property bag. If null or empty, all categories of property are returned. Pass the keyword "none" to return no properties (a valid list of categories can be obtained from the /StopPoint/Meta/categories endpoint)
        categories: Optional[list[str]] = None

        location_lat: Optional[float] = None

        location_lon: Optional[float] = None

        # the list of modes to search (comma separated mode names e.g. tube,dlr)
        modes: Optional[list[str]] = None

        # the radius of the bounding circle in metres (default : 200)
        radius: Optional[int] = None

        # true to return the lines that each stop point serves as a nested resource
        return_lines: Optional[bool] = None

        # a list of stopTypes that should be returned (a list of valid stop types can be obtained from the StopPoint/meta/stoptypes endpoint)
        stop_types: Optional[list[str]] = None

        # Re-arrange the output into a parent/child hierarchy
        use_stop_point_hierarchy: Optional[bool] = None

    
    @dataclass
    class StopPointRequestBuilderGetRequestConfiguration(RequestConfiguration[StopPointRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

