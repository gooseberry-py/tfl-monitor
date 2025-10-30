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
    from ......models.tfl.api.presentation.entities.journey_planner.itinerary_result import ItineraryResult
    from .get_accessibility_preference_query_parameter_type import GetAccessibilityPreferenceQueryParameterType
    from .get_bike_proficiency_query_parameter_type import GetBikeProficiencyQueryParameterType
    from .get_cycle_preference_query_parameter_type import GetCyclePreferenceQueryParameterType
    from .get_journey_preference_query_parameter_type import GetJourneyPreferenceQueryParameterType
    from .get_time_is_query_parameter_type import GetTimeIsQueryParameterType
    from .get_walking_speed_query_parameter_type import GetWalkingSpeedQueryParameterType

class WithToItemRequestBuilder(BaseRequestBuilder):
    """
    Builds and executes requests for operations under /Journey/JourneyResults/{from}/to/{to}
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Union[str, dict[str, Any]]) -> None:
        """
        Instantiates a new WithToItemRequestBuilder and sets the default values.
        param path_parameters: The raw url or the url-template parameters for the request.
        param request_adapter: The request adapter to use to execute the requests.
        Returns: None
        """
        super().__init__(request_adapter, "{+baseurl}/Journey/JourneyResults/{from}/to/{to}{?accessibilityPreference*,adjustment*,alternativeCycle*,alternativeWalking*,applyHtmlMarkup*,bikeProficiency*,calcOneDirection*,combineTransferLegs*,cyclePreference*,date*,fromName*,includeAlternativeRoutes*,journeyPreference*,maxTransferMinutes*,maxWalkingMinutes*,mode*,nationalSearch*,overrideMultiModalScenario*,routeBetweenEntrances*,taxiOnlyTrip*,time*,timeIs*,toName*,useMultiModalCall*,useRealTimeLiveArrivals*,via*,viaName*,walkingOptimization*,walkingSpeed*}", path_parameters)
    
    async def get(self,request_configuration: Optional[RequestConfiguration[WithToItemRequestBuilderGetQueryParameters]] = None) -> Optional[ItineraryResult]:
        """
        Perform a Journey Planner search from the parameters specified in simple types
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[ItineraryResult]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ......models.tfl.api.presentation.entities.journey_planner.itinerary_result import ItineraryResult

        return await self.request_adapter.send_async(request_info, ItineraryResult, None)
    
    def to_get_request_information(self,request_configuration: Optional[RequestConfiguration[WithToItemRequestBuilderGetQueryParameters]] = None) -> RequestInformation:
        """
        Perform a Journey Planner search from the parameters specified in simple types
        param request_configuration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation(Method.GET, self.url_template, self.path_parameters)
        request_info.configure(request_configuration)
        request_info.headers.try_add("Accept", "application/json")
        return request_info
    
    def with_url(self,raw_url: str) -> WithToItemRequestBuilder:
        """
        Returns a request builder with the provided arbitrary URL. Using this method means any other path or query parameters are ignored.
        param raw_url: The raw URL to use for the request builder.
        Returns: WithToItemRequestBuilder
        """
        if raw_url is None:
            raise TypeError("raw_url cannot be null.")
        return WithToItemRequestBuilder(self.request_adapter, raw_url)
    
    @dataclass
    class WithToItemRequestBuilderGetQueryParameters():
        """
        Perform a Journey Planner search from the parameters specified in simple types
        """
        def get_query_parameter(self,original_name: str) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            param original_name: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise TypeError("original_name cannot be null.")
            if original_name == "accessibility_preference":
                return "accessibilityPreference"
            if original_name == "alternative_cycle":
                return "alternativeCycle"
            if original_name == "alternative_walking":
                return "alternativeWalking"
            if original_name == "apply_html_markup":
                return "applyHtmlMarkup"
            if original_name == "bike_proficiency":
                return "bikeProficiency"
            if original_name == "calc_one_direction":
                return "calcOneDirection"
            if original_name == "combine_transfer_legs":
                return "combineTransferLegs"
            if original_name == "cycle_preference":
                return "cyclePreference"
            if original_name == "from_name":
                return "fromName"
            if original_name == "include_alternative_routes":
                return "includeAlternativeRoutes"
            if original_name == "journey_preference":
                return "journeyPreference"
            if original_name == "max_transfer_minutes":
                return "maxTransferMinutes"
            if original_name == "max_walking_minutes":
                return "maxWalkingMinutes"
            if original_name == "national_search":
                return "nationalSearch"
            if original_name == "override_multi_modal_scenario":
                return "overrideMultiModalScenario"
            if original_name == "route_between_entrances":
                return "routeBetweenEntrances"
            if original_name == "taxi_only_trip":
                return "taxiOnlyTrip"
            if original_name == "time_is":
                return "timeIs"
            if original_name == "to_name":
                return "toName"
            if original_name == "use_multi_modal_call":
                return "useMultiModalCall"
            if original_name == "use_real_time_live_arrivals":
                return "useRealTimeLiveArrivals"
            if original_name == "via_name":
                return "viaName"
            if original_name == "walking_optimization":
                return "walkingOptimization"
            if original_name == "walking_speed":
                return "walkingSpeed"
            if original_name == "adjustment":
                return "adjustment"
            if original_name == "date":
                return "date"
            if original_name == "mode":
                return "mode"
            if original_name == "time":
                return "time"
            if original_name == "via":
                return "via"
            return original_name
        
        # The accessibility preference must be a comma separated list eg. "noSolidStairs,noEscalators,noElevators,stepFreeToVehicle,stepFreeToPlatform"
        accessibility_preference: list[GetAccessibilityPreferenceQueryParameterType] = field(default_factory=list)

        # Time adjustment command. eg possible options: "TripFirst" | "TripLast"
        adjustment: Optional[str] = None

        # Option to determine whether to return alternative cycling journey
        alternative_cycle: Optional[bool] = None

        # Option to determine whether to return alternative walking journey
        alternative_walking: Optional[bool] = None

        # Flag to determine whether certain text (e.g. walking instructions) should be output with HTML tags or not.
        apply_html_markup: Optional[bool] = None

        # A comma separated list of cycling proficiency levels. eg possible options: "easy,moderate,fast"
        bike_proficiency: list[GetBikeProficiencyQueryParameterType] = field(default_factory=list)

        # A boolean to make Journey Planner calculate journeys in one temporal direction only. In other words, only calculate journeys after the 'depart' time, or before the 'arrive' time. By default, the Journey Planner engine (EFA) calculates journeys in both temporal directions.
        calc_one_direction: Optional[bool] = None

        # A boolean to indicate whether walking leg to station entrance and walking leg from station entrance to platform should be combined. Defaults to true
        combine_transfer_legs: Optional[bool] = None

        # The cycle preference. eg possible options: "allTheWay" | "leaveAtStation" | "takeOnTransport" | "cycleHire"
        cycle_preference: Optional[GetCyclePreferenceQueryParameterType] = None

        # The date must be in yyyyMMdd format
        date: Optional[str] = None

        # An optional name to associate with the origin of the journey in the results.
        from_name: Optional[str] = None

        # A boolean to make Journey Planner return alternative routes. Alternative routes are calculated by removing one or more lines included in the fastest route and re-calculating. By default, these journeys will not be returned.
        include_alternative_routes: Optional[bool] = None

        # The journey preference eg possible options: "leastinterchange" | "leasttime" | "leastwalking"
        journey_preference: Optional[GetJourneyPreferenceQueryParameterType] = None

        # The max walking time in minutes for transfer eg. "120"
        max_transfer_minutes: Optional[str] = None

        # The max walking time in minutes for journeys eg. "120"
        max_walking_minutes: Optional[str] = None

        # The mode must be a comma separated list of modes. eg possible options: "public-bus,overground,train,tube,coach,dlr,cablecar,tram,river,walking,cycle"
        mode: Optional[list[str]] = None

        # Does the journey cover stops outside London? eg. "nationalSearch=true"
        national_search: Optional[bool] = None

        # An optional integer to indicate what multi modal scenario we want to use.
        override_multi_modal_scenario: Optional[int] = None

        # A boolean to indicate whether public transport routes should include directions between platforms and station entrances.
        route_between_entrances: Optional[bool] = None

        # A boolean to indicate whether to return one or more taxi journeys. Note, setting this to true will override "useMultiModalCall".
        taxi_only_trip: Optional[bool] = None

        # The time must be in HHmm format
        time: Optional[str] = None

        # Does the time given relate to arrival or leaving time? Possible options: "departing" | "arriving"
        time_is: Optional[GetTimeIsQueryParameterType] = None

        # An optional name to associate with the destination of the journey in the results.
        to_name: Optional[str] = None

        # A boolean to indicate whether or not to return 3 public transport journeys, a bus journey, a cycle hire journey, a personal cycle journey and a walking journey
        use_multi_modal_call: Optional[bool] = None

        # A boolean to indicate if we want to receive real time live arrivals data where available.
        use_real_time_live_arrivals: Optional[bool] = None

        # Travel through point on the journey. Can be WGS84 coordinates expressed as "lat,long", a UK postcode, a Naptan (StopPoint) id, an ICS StopId, or a free-text string (will cause disambiguation unless it exactly matches a point of interest name).
        via: Optional[str] = None

        # An optional name to associate with the via point of the journey in the results.
        via_name: Optional[str] = None

        # A boolean to indicate whether to optimize journeys using walking
        walking_optimization: Optional[bool] = None

        # The walking speed. eg possible options: "slow" | "average" | "fast".
        walking_speed: Optional[GetWalkingSpeedQueryParameterType] = None

    
    @dataclass
    class WithToItemRequestBuilderGetRequestConfiguration(RequestConfiguration[WithToItemRequestBuilderGetQueryParameters]):
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        warn("This class is deprecated. Please use the generic RequestConfiguration class generated by the generator.", DeprecationWarning)
    

