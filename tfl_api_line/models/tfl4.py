from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Tfl4(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Direction in regards to Journey Planner i.e. inbound or outbound
    direction: Optional[str] = None
    # The Line Name e.g. "Victoria"
    line: Optional[str] = None
    # Direction of the Line e.g. NB, SB, WB etc.
    line_direction: Optional[str] = None
    # Naptan of the adjacent station
    naptan_to: Optional[str] = None
    # Direction displayed on the platform e.g. NB, SB, WB etc.
    platform_direction: Optional[str] = None
    # Time in 24hr format with 15 minute intervals e.g. 0500-0515, 0515-0530 etc.
    time_slice: Optional[str] = None
    # Scale between 1-6,              1 = Very quiet, 2 = Quiet, 3 = Fairly busy, 4 = Busy, 5 = Very busy, 6 = Exceptionally busy
    value: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl4:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl4
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl4()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "line": lambda n : setattr(self, 'line', n.get_str_value()),
            "lineDirection": lambda n : setattr(self, 'line_direction', n.get_str_value()),
            "naptanTo": lambda n : setattr(self, 'naptan_to', n.get_str_value()),
            "platformDirection": lambda n : setattr(self, 'platform_direction', n.get_str_value()),
            "timeSlice": lambda n : setattr(self, 'time_slice', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_int_value()),
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
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("line", self.line)
        writer.write_str_value("lineDirection", self.line_direction)
        writer.write_str_value("naptanTo", self.naptan_to)
        writer.write_str_value("platformDirection", self.platform_direction)
        writer.write_str_value("timeSlice", self.time_slice)
        writer.write_int_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

