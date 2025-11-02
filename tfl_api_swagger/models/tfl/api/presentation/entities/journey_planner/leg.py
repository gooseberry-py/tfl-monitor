from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..disruption import Disruption
    from ..identifier import Identifier
    from ..instruction import Instruction
    from ..point import Point
    from .obstacle import Obstacle
    from .path import Path
    from .planned_work import PlannedWork
    from .route_option import RouteOption

@dataclass
class Leg(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Represents a point located at a latitude and longitude using the WGS84 co-ordinate system.
    arrival_point: Optional[Point] = None
    # The arrivalTime property
    arrival_time: Optional[datetime.datetime] = None
    # Represents a point located at a latitude and longitude using the WGS84 co-ordinate system.
    departure_point: Optional[Point] = None
    # The departureTime property
    departure_time: Optional[datetime.datetime] = None
    # The disruptions property
    disruptions: Optional[list[Disruption]] = None
    # The distance property
    distance: Optional[float] = None
    # The duration property
    duration: Optional[int] = None
    # The hasFixedLocations property
    has_fixed_locations: Optional[bool] = None
    # The instruction property
    instruction: Optional[Instruction] = None
    # The interChangeDuration property
    inter_change_duration: Optional[str] = None
    # The interChangePosition property
    inter_change_position: Optional[str] = None
    # The isDisrupted property
    is_disrupted: Optional[bool] = None
    # The mode property
    mode: Optional[Identifier] = None
    # The obstacles property
    obstacles: Optional[list[Obstacle]] = None
    # The path property
    path: Optional[Path] = None
    # The plannedWorks property
    planned_works: Optional[list[PlannedWork]] = None
    # The routeOptions property
    route_options: Optional[list[RouteOption]] = None
    # The scheduledArrivalTime property
    scheduled_arrival_time: Optional[datetime.datetime] = None
    # The scheduledDepartureTime property
    scheduled_departure_time: Optional[datetime.datetime] = None
    # The speed property
    speed: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Leg:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Leg
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Leg()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..disruption import Disruption
        from ..identifier import Identifier
        from ..instruction import Instruction
        from ..point import Point
        from .obstacle import Obstacle
        from .path import Path
        from .planned_work import PlannedWork
        from .route_option import RouteOption

        from ..disruption import Disruption
        from ..identifier import Identifier
        from ..instruction import Instruction
        from ..point import Point
        from .obstacle import Obstacle
        from .path import Path
        from .planned_work import PlannedWork
        from .route_option import RouteOption

        fields: dict[str, Callable[[Any], None]] = {
            "arrivalPoint": lambda n : setattr(self, 'arrival_point', n.get_object_value(Point)),
            "arrivalTime": lambda n : setattr(self, 'arrival_time', n.get_datetime_value()),
            "departurePoint": lambda n : setattr(self, 'departure_point', n.get_object_value(Point)),
            "departureTime": lambda n : setattr(self, 'departure_time', n.get_datetime_value()),
            "disruptions": lambda n : setattr(self, 'disruptions', n.get_collection_of_object_values(Disruption)),
            "distance": lambda n : setattr(self, 'distance', n.get_float_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "hasFixedLocations": lambda n : setattr(self, 'has_fixed_locations', n.get_bool_value()),
            "instruction": lambda n : setattr(self, 'instruction', n.get_object_value(Instruction)),
            "interChangeDuration": lambda n : setattr(self, 'inter_change_duration', n.get_str_value()),
            "interChangePosition": lambda n : setattr(self, 'inter_change_position', n.get_str_value()),
            "isDisrupted": lambda n : setattr(self, 'is_disrupted', n.get_bool_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_object_value(Identifier)),
            "obstacles": lambda n : setattr(self, 'obstacles', n.get_collection_of_object_values(Obstacle)),
            "path": lambda n : setattr(self, 'path', n.get_object_value(Path)),
            "plannedWorks": lambda n : setattr(self, 'planned_works', n.get_collection_of_object_values(PlannedWork)),
            "routeOptions": lambda n : setattr(self, 'route_options', n.get_collection_of_object_values(RouteOption)),
            "scheduledArrivalTime": lambda n : setattr(self, 'scheduled_arrival_time', n.get_datetime_value()),
            "scheduledDepartureTime": lambda n : setattr(self, 'scheduled_departure_time', n.get_datetime_value()),
            "speed": lambda n : setattr(self, 'speed', n.get_str_value()),
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
        writer.write_object_value("arrivalPoint", self.arrival_point)
        writer.write_datetime_value("arrivalTime", self.arrival_time)
        writer.write_object_value("departurePoint", self.departure_point)
        writer.write_datetime_value("departureTime", self.departure_time)
        writer.write_collection_of_object_values("disruptions", self.disruptions)
        writer.write_float_value("distance", self.distance)
        writer.write_int_value("duration", self.duration)
        writer.write_object_value("instruction", self.instruction)
        writer.write_str_value("interChangeDuration", self.inter_change_duration)
        writer.write_str_value("interChangePosition", self.inter_change_position)
        writer.write_object_value("mode", self.mode)
        writer.write_collection_of_object_values("obstacles", self.obstacles)
        writer.write_object_value("path", self.path)
        writer.write_collection_of_object_values("plannedWorks", self.planned_works)
        writer.write_collection_of_object_values("routeOptions", self.route_options)
        writer.write_datetime_value("scheduledArrivalTime", self.scheduled_arrival_time)
        writer.write_datetime_value("scheduledDepartureTime", self.scheduled_departure_time)
        writer.write_str_value("speed", self.speed)
        writer.write_additional_data_value(self.additional_data)
    

