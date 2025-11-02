from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DbGeographyWellKnownValue(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The coordinateSystemId property
    coordinate_system_id: Optional[int] = None
    # The wellKnownBinary property
    well_known_binary: Optional[bytes] = None
    # The wellKnownText property
    well_known_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DbGeographyWellKnownValue:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DbGeographyWellKnownValue
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DbGeographyWellKnownValue()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "coordinateSystemId": lambda n : setattr(self, 'coordinate_system_id', n.get_int_value()),
            "wellKnownBinary": lambda n : setattr(self, 'well_known_binary', n.get_bytes_value()),
            "wellKnownText": lambda n : setattr(self, 'well_known_text', n.get_str_value()),
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
        writer.write_int_value("coordinateSystemId", self.coordinate_system_id)
        writer.write_bytes_value("wellKnownBinary", self.well_known_binary)
        writer.write_str_value("wellKnownText", self.well_known_text)
        writer.write_additional_data_value(self.additional_data)
    

