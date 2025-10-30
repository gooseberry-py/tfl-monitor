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
    from .............models.system.object import Object
    from .get_direction_query_parameter_type import GetDirectionQueryParameterType

class WithHeightItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /TravelTimes/compareOverlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}/{height}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithHeightItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/TravelTimes/compareOverlay/{z}/mapcenter/{mapCenterLat}/{mapCenterLon}/pinlocation/{pinLat}/{pinLon}/dimensions/{width}/{height}?compareType={compareType}&compareValue={compareValue}&direction={direction}&modeId={modeId}&scenarioTitle={scenarioTitle}&timeOfDayId={timeOfDayId}&travelTimeInterval={travelTimeInterval}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithHeightItemRequestBuilderGetQueryParameters]] = None) -> Optional[object]:
        """
        Gets the TravelTime overlay.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[object]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from .............models.system.object import Object

        return await self.request_adapter.send_async(request_info, object, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithHeightItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets the TravelTime overlay.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithHeightItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithHeightItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithHeightItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithHeightItemRequestBuilderGetQueryParameters():
        """
        Gets the TravelTime overlay.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "compare_type":
                return "compareType"
            if original_name == "compare_value":
                return "compareValue"
            if original_name == "mode_id":
                return "modeId"
            if original_name == "scenario_title":
                return "scenarioTitle"
            if original_name == "time_of_day_id":
                return "timeOfDayId"
            if original_name == "travel_time_interval":
                return "travelTimeInterval"
            if original_name == "direction":
                return "direction"
            return original_name
        
        compare_type: Optional[str] = None

        compare_value: Optional[str] = None

        # The direction of travel.
        direction: Optional[GetDirectionQueryParameterType] = None

        # The id of the mode.
        mode_id: Optional[str] = None

        # The title of the scenario.
        scenario_title: Optional[str] = None

        # The id for the time of day (AM/INTER/PM)
        time_of_day_id: Optional[str] = None

        # The total minutes between the travel time bands
        travel_time_interval: Optional[int] = None

    
    @dataclass
    class WithHeightItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithHeightItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

