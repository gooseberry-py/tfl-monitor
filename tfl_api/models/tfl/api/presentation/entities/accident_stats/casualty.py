from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Casualty(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The age property
    age: Optional[int] = None
    # The ageBand property
    age_band: Optional[str] = None
    # The class property
    class_: Optional[str] = None
    # The mode property
    mode: Optional[str] = None
    # The severity property
    severity: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Casualty:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Casualty
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Casualty()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "age": lambda n : setattr(self, 'age', n.get_int_value()),
            "ageBand": lambda n : setattr(self, 'age_band', n.get_str_value()),
            "class": lambda n : setattr(self, 'class_', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_str_value()),
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
        writer.write_int_value("age", self.age)
        writer.write_str_value("ageBand", self.age_band)
        writer.write_str_value("class", self.class_)
        writer.write_str_value("mode", self.mode)
        writer.write_str_value("severity", self.severity)
        writer.write_additional_data_value(self.additional_data)
    

