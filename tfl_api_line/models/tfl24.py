from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Tfl24(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The destination property
    destination: Optional[str] = None
    # The direction property
    direction: Optional[str] = None
    # The fromStation property
    from_station: Optional[str] = None
    # The routeId property
    route_id: Optional[int] = None
    # The serviceType property
    service_type: Optional[str] = None
    # The toStation property
    to_station: Optional[str] = None
    # The vehicleDestinationText property
    vehicle_destination_text: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl24:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl24
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl24()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "destination": lambda n : setattr(self, 'destination', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "fromStation": lambda n : setattr(self, 'from_station', n.get_str_value()),
            "routeId": lambda n : setattr(self, 'route_id', n.get_int_value()),
            "serviceType": lambda n : setattr(self, 'service_type', n.get_str_value()),
            "toStation": lambda n : setattr(self, 'to_station', n.get_str_value()),
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
        writer.write_str_value("destination", self.destination)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("fromStation", self.from_station)
        writer.write_int_value("routeId", self.route_id)
        writer.write_str_value("serviceType", self.service_type)
        writer.write_str_value("toStation", self.to_station)
        writer.write_str_value("vehicleDestinationText", self.vehicle_destination_text)
        writer.write_additional_data_value(self.additional_data)
    

