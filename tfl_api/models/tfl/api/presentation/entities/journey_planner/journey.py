from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .journey_fare import JourneyFare
    from .leg import Leg

@dataclass
class Journey(AdditionalDataHolder, Parsable):
    """
    Object that represents an end to end journey (see schematic).
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The alternativeRoute property
    alternative_route: Optional[bool] = None
    # The arrivalDateTime property
    arrival_date_time: Optional[datetime.datetime] = None
    # The description property
    description: Optional[str] = None
    # The duration property
    duration: Optional[int] = None
    # The fare property
    fare: Optional[JourneyFare] = None
    # The legs property
    legs: Optional[list[Leg]] = None
    # The startDateTime property
    start_date_time: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Journey:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Journey
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Journey()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .journey_fare import JourneyFare
        from .leg import Leg

        from .journey_fare import JourneyFare
        from .leg import Leg

        fields: dict[str, Callable[[Any], None]] = {
            "alternativeRoute": lambda n : setattr(self, 'alternative_route', n.get_bool_value()),
            "arrivalDateTime": lambda n : setattr(self, 'arrival_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "duration": lambda n : setattr(self, 'duration', n.get_int_value()),
            "fare": lambda n : setattr(self, 'fare', n.get_object_value(JourneyFare)),
            "legs": lambda n : setattr(self, 'legs', n.get_collection_of_object_values(Leg)),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
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
        writer.write_bool_value("alternativeRoute", self.alternative_route)
        writer.write_datetime_value("arrivalDateTime", self.arrival_date_time)
        writer.write_str_value("description", self.description)
        writer.write_int_value("duration", self.duration)
        writer.write_object_value("fare", self.fare)
        writer.write_collection_of_object_values("legs", self.legs)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_additional_data_value(self.additional_data)
    

