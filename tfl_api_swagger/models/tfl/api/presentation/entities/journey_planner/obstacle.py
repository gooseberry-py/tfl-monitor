from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Obstacle(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The incline property
    incline: Optional[str] = None
    # The position property
    position: Optional[str] = None
    # The stopId property
    stop_id: Optional[int] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Obstacle:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Obstacle
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Obstacle()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "incline": lambda n : setattr(self, 'incline', n.get_str_value()),
            "position": lambda n : setattr(self, 'position', n.get_str_value()),
            "stopId": lambda n : setattr(self, 'stop_id', n.get_int_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("incline", self.incline)
        writer.write_str_value("position", self.position)
        writer.write_int_value("stopId", self.stop_id)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

