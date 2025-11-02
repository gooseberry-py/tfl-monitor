from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StreetSegment(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # geoJSON formatted LineString containing two latitude/longitude (WGS84) pairs that identify the start and end points of the street segment.
    line_string: Optional[str] = None
    # The ID from the source system of the disruption that this street belongs to.
    source_system_id: Optional[int] = None
    # The key of the source system of the disruption that this street belongs to.
    source_system_key: Optional[str] = None
    # A 16 digit unique integer identifying a OS ITN (Ordnance Survey Integrated Transport Network) road link.
    toid: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StreetSegment:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StreetSegment
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StreetSegment()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "lineString": lambda n : setattr(self, 'line_string', n.get_str_value()),
            "sourceSystemId": lambda n : setattr(self, 'source_system_id', n.get_int_value()),
            "sourceSystemKey": lambda n : setattr(self, 'source_system_key', n.get_str_value()),
            "toid": lambda n : setattr(self, 'toid', n.get_str_value()),
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
        writer.write_str_value("lineString", self.line_string)
        writer.write_int_value("sourceSystemId", self.source_system_id)
        writer.write_str_value("sourceSystemKey", self.source_system_key)
        writer.write_str_value("toid", self.toid)
        writer.write_additional_data_value(self.additional_data)
    

