from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..line import Line
    from .journey import Journey
    from .journey_planner_cycle_hire_docking_station_data import JourneyPlannerCycleHireDockingStationData
    from .journey_vector import JourneyVector
    from .search_criteria import SearchCriteria

@dataclass
class ItineraryResult(AdditionalDataHolder, Parsable):
    """
    A DTO representing a list of possible journeys.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The cycleHireDockingStationData property
    cycle_hire_docking_station_data: Optional[JourneyPlannerCycleHireDockingStationData] = None
    # The journeyVector property
    journey_vector: Optional[JourneyVector] = None
    # The journeys property
    journeys: Optional[list[Journey]] = None
    # The lines property
    lines: Optional[list[Line]] = None
    # The recommendedMaxAgeMinutes property
    recommended_max_age_minutes: Optional[int] = None
    # The searchCriteria property
    search_criteria: Optional[SearchCriteria] = None
    # The stopMessages property
    stop_messages: Optional[list[str]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ItineraryResult:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ItineraryResult
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ItineraryResult()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..line import Line
        from .journey import Journey
        from .journey_planner_cycle_hire_docking_station_data import JourneyPlannerCycleHireDockingStationData
        from .journey_vector import JourneyVector
        from .search_criteria import SearchCriteria

        from ..line import Line
        from .journey import Journey
        from .journey_planner_cycle_hire_docking_station_data import JourneyPlannerCycleHireDockingStationData
        from .journey_vector import JourneyVector
        from .search_criteria import SearchCriteria

        fields: dict[str, Callable[[Any], None]] = {
            "cycleHireDockingStationData": lambda n : setattr(self, 'cycle_hire_docking_station_data', n.get_object_value(JourneyPlannerCycleHireDockingStationData)),
            "journeyVector": lambda n : setattr(self, 'journey_vector', n.get_object_value(JourneyVector)),
            "journeys": lambda n : setattr(self, 'journeys', n.get_collection_of_object_values(Journey)),
            "lines": lambda n : setattr(self, 'lines', n.get_collection_of_object_values(Line)),
            "recommendedMaxAgeMinutes": lambda n : setattr(self, 'recommended_max_age_minutes', n.get_int_value()),
            "searchCriteria": lambda n : setattr(self, 'search_criteria', n.get_object_value(SearchCriteria)),
            "stopMessages": lambda n : setattr(self, 'stop_messages', n.get_collection_of_primitive_values(str)),
        }
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        param writer: Serialization writer to use to serialize this model
        Returns: None
        """
        if writer is None:
            raise TypeError("writer cannot be null.")
        writer.write_object_value("cycleHireDockingStationData", self.cycle_hire_docking_station_data)
        writer.write_object_value("journeyVector", self.journey_vector)
        writer.write_collection_of_object_values("journeys", self.journeys)
        writer.write_collection_of_object_values("lines", self.lines)
        writer.write_int_value("recommendedMaxAgeMinutes", self.recommended_max_age_minutes)
        writer.write_object_value("searchCriteria", self.search_criteria)
        writer.write_collection_of_primitive_values("stopMessages", self.stop_messages)
        writer.write_additional_data_value(self.additional_data)
    

