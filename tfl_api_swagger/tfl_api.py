from __future__ import annotations
from collections.abc import Callable
from kiota_abstractions.api_client_builder import enable_backing_store_for_serialization_writer_factory, register_default_deserializer, register_default_serializer
from kiota_abstractions.base_request_builder import BaseRequestBuilder
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.serialization import ParseNodeFactoryRegistry, SerializationWriterFactoryRegistry
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .accident_stats.accident_stats_request_builder import AccidentStatsRequestBuilder
    from .air_quality.air_quality_request_builder import AirQualityRequestBuilder
    from .bike_point.bike_point_request_builder import BikePointRequestBuilder
    from .cabwise.cabwise_request_builder import CabwiseRequestBuilder
    from .journey.journey_request_builder import JourneyRequestBuilder
    from .line.line_request_builder import LineRequestBuilder
    from .mode.mode_request_builder import ModeRequestBuilder
    from .occupancy.occupancy_request_builder import OccupancyRequestBuilder
    from .place.place_request_builder import PlaceRequestBuilder
    from .road.road_request_builder import RoadRequestBuilder
    from .search.search_request_builder import SearchRequestBuilder
    from .stop_point.stop_point_request_builder import StopPointRequestBuilder
    from .travel_times.travel_times_request_builder import TravelTimesRequestBuilder
    from .vehicle.vehicle_request_builder import VehicleRequestBuilder

class Tfl_api(BaseRequestBuilder):
    """
    The main entry point of the SDK, exposes the configuration and the fluent API.
    """
    def __init__(self,request_adapter: RequestAdapter) -> None:
        """
        Instantiates a new Tfl_api and sets the default values.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        if request_adapter is None:
            raise TypeError("request_adapter cannot be null.")
        super().__init__(request_adapter, "{+baseurl}", None)
        if not self.request_adapter.base_url:
            self.request_adapter.base_url = "https://api.tfl.gov.uk"
        self.path_parameters["base_url"] = self.request_adapter.base_url
    
    @property
    def accident_stats(self) -> AccidentStatsRequestBuilder:
        """
        The AccidentStats property
        """
        from .accident_stats.accident_stats_request_builder import AccidentStatsRequestBuilder

        return AccidentStatsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def air_quality(self) -> AirQualityRequestBuilder:
        """
        The AirQuality property
        """
        from .air_quality.air_quality_request_builder import AirQualityRequestBuilder

        return AirQualityRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def bike_point(self) -> BikePointRequestBuilder:
        """
        The BikePoint property
        """
        from .bike_point.bike_point_request_builder import BikePointRequestBuilder

        return BikePointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def cabwise(self) -> CabwiseRequestBuilder:
        """
        The Cabwise property
        """
        from .cabwise.cabwise_request_builder import CabwiseRequestBuilder

        return CabwiseRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def journey(self) -> JourneyRequestBuilder:
        """
        The Journey property
        """
        from .journey.journey_request_builder import JourneyRequestBuilder

        return JourneyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def line(self) -> LineRequestBuilder:
        """
        The Line property
        """
        from .line.line_request_builder import LineRequestBuilder

        return LineRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def mode(self) -> ModeRequestBuilder:
        """
        The Mode property
        """
        from .mode.mode_request_builder import ModeRequestBuilder

        return ModeRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def occupancy(self) -> OccupancyRequestBuilder:
        """
        The Occupancy property
        """
        from .occupancy.occupancy_request_builder import OccupancyRequestBuilder

        return OccupancyRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def place(self) -> PlaceRequestBuilder:
        """
        The Place property
        """
        from .place.place_request_builder import PlaceRequestBuilder

        return PlaceRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def road(self) -> RoadRequestBuilder:
        """
        The Road property
        """
        from .road.road_request_builder import RoadRequestBuilder

        return RoadRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def search(self) -> SearchRequestBuilder:
        """
        The Search property
        """
        from .search.search_request_builder import SearchRequestBuilder

        return SearchRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def stop_point(self) -> StopPointRequestBuilder:
        """
        The StopPoint property
        """
        from .stop_point.stop_point_request_builder import StopPointRequestBuilder

        return StopPointRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def travel_times(self) -> TravelTimesRequestBuilder:
        """
        The TravelTimes property
        """
        from .travel_times.travel_times_request_builder import TravelTimesRequestBuilder

        return TravelTimesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def vehicle(self) -> VehicleRequestBuilder:
        """
        The Vehicle property
        """
        from .vehicle.vehicle_request_builder import VehicleRequestBuilder

        return VehicleRequestBuilder(self.request_adapter, self.path_parameters)
    

