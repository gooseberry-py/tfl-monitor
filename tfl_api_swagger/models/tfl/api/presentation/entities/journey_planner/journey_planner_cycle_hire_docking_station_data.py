from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JourneyPlannerCycleHireDockingStationData(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The destinationId property
    destination_id: Optional[str] = None
    # The destinationNumberOfBikes property
    destination_number_of_bikes: Optional[int] = None
    # The destinationNumberOfEmptySlots property
    destination_number_of_empty_slots: Optional[int] = None
    # The originId property
    origin_id: Optional[str] = None
    # The originNumberOfBikes property
    origin_number_of_bikes: Optional[int] = None
    # The originNumberOfEmptySlots property
    origin_number_of_empty_slots: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JourneyPlannerCycleHireDockingStationData:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JourneyPlannerCycleHireDockingStationData
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JourneyPlannerCycleHireDockingStationData()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "destinationId": lambda n : setattr(self, 'destination_id', n.get_str_value()),
            "destinationNumberOfBikes": lambda n : setattr(self, 'destination_number_of_bikes', n.get_int_value()),
            "destinationNumberOfEmptySlots": lambda n : setattr(self, 'destination_number_of_empty_slots', n.get_int_value()),
            "originId": lambda n : setattr(self, 'origin_id', n.get_str_value()),
            "originNumberOfBikes": lambda n : setattr(self, 'origin_number_of_bikes', n.get_int_value()),
            "originNumberOfEmptySlots": lambda n : setattr(self, 'origin_number_of_empty_slots', n.get_int_value()),
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
        writer.write_str_value("destinationId", self.destination_id)
        writer.write_int_value("destinationNumberOfBikes", self.destination_number_of_bikes)
        writer.write_int_value("destinationNumberOfEmptySlots", self.destination_number_of_empty_slots)
        writer.write_str_value("originId", self.origin_id)
        writer.write_int_value("originNumberOfBikes", self.origin_number_of_bikes)
        writer.write_int_value("originNumberOfEmptySlots", self.origin_number_of_empty_slots)
        writer.write_additional_data_value(self.additional_data)
    

