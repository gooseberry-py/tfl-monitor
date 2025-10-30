from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class StopPointRouteSection(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The destinationName property
    destination_name: Optional[str] = None
    # The direction property
    direction: Optional[str] = None
    # The isActive property
    is_active: Optional[bool] = None
    # The lineId property
    line_id: Optional[str] = None
    # The lineString property
    line_string: Optional[str] = None
    # The mode property
    mode: Optional[str] = None
    # The naptanId property
    naptan_id: Optional[str] = None
    # The routeSectionName property
    route_section_name: Optional[str] = None
    # The serviceType property
    service_type: Optional[str] = None
    # The validFrom property
    valid_from: Optional[datetime.datetime] = None
    # The validTo property
    valid_to: Optional[datetime.datetime] = None
    # The vehicleDestinationText property
    vehicle_destination_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StopPointRouteSection:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StopPointRouteSection
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StopPointRouteSection()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "isActive": lambda n : setattr(self, 'is_active', n.get_bool_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineString": lambda n : setattr(self, 'line_string', n.get_str_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "naptanId": lambda n : setattr(self, 'naptan_id', n.get_str_value()),
            "routeSectionName": lambda n : setattr(self, 'route_section_name', n.get_str_value()),
            "serviceType": lambda n : setattr(self, 'service_type', n.get_str_value()),
            "validFrom": lambda n : setattr(self, 'valid_from', n.get_datetime_value()),
            "validTo": lambda n : setattr(self, 'valid_to', n.get_datetime_value()),
            "vehicleDestinationText": lambda n : setattr(self, 'vehicle_destination_text', n.get_str_value()),
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
        writer.write_bool_value("isActive", self.is_active)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineString", self.line_string)
        writer.write_str_value("mode", self.mode)
        writer.write_str_value("naptanId", self.naptan_id)
        writer.write_str_value("routeSectionName", self.route_section_name)
        writer.write_str_value("serviceType", self.service_type)
        writer.write_datetime_value("validFrom", self.valid_from)
        writer.write_datetime_value("validTo", self.valid_to)
        writer.write_str_value("vehicleDestinationText", self.vehicle_destination_text)
        writer.write_additional_data_value(self.additional_data)
    

