from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl12 import Tfl12

@dataclass
class Tfl13(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The name of the Destination StopPoint
    destination_name: Optional[str] = None
    # Inbound or Outbound
    direction: Optional[str] = None
    # The Id of the route
    id: Optional[str] = None
    # The Id of the Line
    line_id: Optional[str] = None
    # The co-ordinates of the route's path as a geoJSON lineString
    line_string: Optional[str] = None
    # Name such as "72"
    name: Optional[str] = None
    # The name of the Origin StopPoint
    origination_name: Optional[str] = None
    # The route code
    route_code: Optional[str] = None
    # The routeSectionNaptanEntrySequence property
    route_section_naptan_entry_sequence: Optional[list[Tfl12]] = None
    # The DateTime that the Service containing this Route is valid from.
    valid_from: Optional[datetime.datetime] = None
    # The DateTime that the Service containing this Route is valid until.
    valid_to: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl13:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl13
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl13()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl12 import Tfl12

        from .tfl12 import Tfl12

        fields: dict[str, Callable[[Any], None]] = {
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineString": lambda n : setattr(self, 'line_string', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "originationName": lambda n : setattr(self, 'origination_name', n.get_str_value()),
            "routeCode": lambda n : setattr(self, 'route_code', n.get_str_value()),
            "routeSectionNaptanEntrySequence": lambda n : setattr(self, 'route_section_naptan_entry_sequence', n.get_collection_of_object_values(Tfl12)),
            "validFrom": lambda n : setattr(self, 'valid_from', n.get_datetime_value()),
            "validTo": lambda n : setattr(self, 'valid_to', n.get_datetime_value()),
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
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("id", self.id)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineString", self.line_string)
        writer.write_str_value("name", self.name)
        writer.write_str_value("originationName", self.origination_name)
        writer.write_str_value("routeCode", self.route_code)
        writer.write_collection_of_object_values("routeSectionNaptanEntrySequence", self.route_section_naptan_entry_sequence)
        writer.write_datetime_value("validFrom", self.valid_from)
        writer.write_datetime_value("validTo", self.valid_to)
        writer.write_additional_data_value(self.additional_data)
    

