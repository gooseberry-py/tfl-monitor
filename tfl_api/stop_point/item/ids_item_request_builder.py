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
    from ...models.tfl.api.presentation.entities.stop_point import StopPoint
    from .arrivals.arrivals_request_builder import ArrivalsRequestBuilder
    from .arrival_departures.arrival_departures_request_builder import ArrivalDeparturesRequestBuilder
    from .can_reach_on_line.can_reach_on_line_request_builder import CanReachOnLineRequestBuilder
    from .car_parks.car_parks_request_builder import CarParksRequestBuilder
    from .crowding.crowding_request_builder import CrowdingRequestBuilder
    from .direction_to.direction_to_request_builder import DirectionToRequestBuilder
    from .disruption.disruption_request_builder import DisruptionRequestBuilder
    from .place_types.place_types_request_builder import PlaceTypesRequestBuilder
    from .route.route_request_builder import RouteRequestBuilder
    from .taxi_ranks.taxi_ranks_request_builder import TaxiRanksRequestBuilder

class IdsItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /StopPoint/{ids-id}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new IdsItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/StopPoint/{ids%2Did}{?includeCrowdingData*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[IdsItemRequestBuilderGetQueryParameters]] = None) -> Optional[list[StopPoint]]:
        """
        Gets a list of StopPoints corresponding to the given list of stop ids.
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[list[StopPoint]]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models.tfl.api.presentation.entities.stop_point import StopPoint

        return await self.request_adapter.send_collection_async(request_info, StopPoint, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[IdsItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Gets a list of StopPoints corresponding to the given list of stop ids.
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
    def arrival_departures(self) -> ArrivalDeparturesRequestBuilder:
        """
        The ArrivalDepartures property
        """
        from .arrival_departures.arrival_departures_request_builder import ArrivalDeparturesRequestBuilder

        return ArrivalDeparturesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def arrivals(self) -> ArrivalsRequestBuilder:
        """
        The Arrivals property
        """
        from .arrivals.arrivals_request_builder import ArrivalsRequestBuilder

        return ArrivalsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def can_reach_on_line(self) -> CanReachOnLineRequestBuilder:
        """
        The CanReachOnLine property
        """
        from .can_reach_on_line.can_reach_on_line_request_builder import CanReachOnLineRequestBuilder

        return CanReachOnLineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def car_parks(self) -> CarParksRequestBuilder:
        """
        The CarParks property
        """
        from .car_parks.car_parks_request_builder import CarParksRequestBuilder

        return CarParksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def crowding(self) -> CrowdingRequestBuilder:
        """
        The Crowding property
        """
        from .crowding.crowding_request_builder import CrowdingRequestBuilder

        return CrowdingRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def direction_to(self) -> DirectionToRequestBuilder:
        """
        The DirectionTo property
        """
        from .direction_to.direction_to_request_builder import DirectionToRequestBuilder

        return DirectionToRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def disruption(self) -> DisruptionRequestBuilder:
        """
        The Disruption property
        """
        from .disruption.disruption_request_builder import DisruptionRequestBuilder

        return DisruptionRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def place_types(self) -> PlaceTypesRequestBuilder:
        """
        The placeTypes property
        """
        from .place_types.place_types_request_builder import PlaceTypesRequestBuilder

        return PlaceTypesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def route(self) -> RouteRequestBuilder:
        """
        The Route property
        """
        from .route.route_request_builder import RouteRequestBuilder

        return RouteRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def taxi_ranks(self) -> TaxiRanksRequestBuilder:
        """
        The TaxiRanks property
        """
        from .taxi_ranks.taxi_ranks_request_builder import TaxiRanksRequestBuilder

        return TaxiRanksRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class IdsItemRequestBuilderGetQueryParameters():
        """
        Gets a list of StopPoints corresponding to the given list of stop ids.
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "include_crowding_data":
                return "includeCrowdingData"
            return original_name
        
        # Include the crowding data (static). To Filter further use: /StopPoint/{ids}/Crowding/{line}
        include_crowding_data: Optional[bool] = None

    
    @dataclass
    class IdsItemRequestBuilderGetRequestConfiguration(RequestConfiguration[IdsItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

