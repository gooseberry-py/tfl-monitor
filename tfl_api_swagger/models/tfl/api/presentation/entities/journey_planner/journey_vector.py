from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JourneyVector(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The from property
    from_: Optional[str] = None
    # The to property
    to: Optional[str] = None
    # The uri property
    uri: Optional[str] = None
    # The via property
    via: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JourneyVector:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JourneyVector
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JourneyVector()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "from": lambda n : setattr(self, 'from_', n.get_str_value()),
            "to": lambda n : setattr(self, 'to', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
            "via": lambda n : setattr(self, 'via', n.get_str_value()),
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
        writer.write_str_value("from", self.from_)
        writer.write_str_value("to", self.to)
        writer.write_str_value("uri", self.uri)
        writer.write_str_value("via", self.via)
        writer.write_additional_data_value(self.additional_data)
    

