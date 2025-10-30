from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Mode(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The isFarePaying property
    is_fare_paying: Optional[bool] = None
    # The isScheduledService property
    is_scheduled_service: Optional[bool] = None
    # The isTflService property
    is_tfl_service: Optional[bool] = None
    # The modeName property
    mode_name: Optional[str] = None
    # The motType property
    mot_type: Optional[str] = None
    # The network property
    network: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Mode:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Mode
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Mode()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "isFarePaying": lambda n : setattr(self, 'is_fare_paying', n.get_bool_value()),
            "isScheduledService": lambda n : setattr(self, 'is_scheduled_service', n.get_bool_value()),
            "isTflService": lambda n : setattr(self, 'is_tfl_service', n.get_bool_value()),
            "modeName": lambda n : setattr(self, 'mode_name', n.get_str_value()),
            "motType": lambda n : setattr(self, 'mot_type', n.get_str_value()),
            "network": lambda n : setattr(self, 'network', n.get_str_value()),
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
        writer.write_bool_value("isFarePaying", self.is_fare_paying)
        writer.write_bool_value("isScheduledService", self.is_scheduled_service)
        writer.write_bool_value("isTflService", self.is_tfl_service)
        writer.write_str_value("modeName", self.mode_name)
        writer.write_str_value("motType", self.mot_type)
        writer.write_str_value("network", self.network)
        writer.write_additional_data_value(self.additional_data)
    

