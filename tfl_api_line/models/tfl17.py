from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Tfl17(AdditionalDataHolder, Parsable):
    """
    Description of a Route used in Route search results.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Id (NaPTAN code) or the Destination StopPoint
    destination: Optional[str] = None
    # The name of the Destination StopPoint
    destination_name: Optional[str] = None
    # Inbound or Outbound
    direction: Optional[str] = None
    # Name such as "72"
    name: Optional[str] = None
    # The name of the Origin StopPoint
    origination_name: Optional[str] = None
    # The Id (NaPTAN code) of the Origin StopPoint
    originator: Optional[str] = None
    # The route code
    route_code: Optional[str] = None
    # Regular or Night
    service_type: Optional[str] = None
    # The DateTime that the Service containing this Route is valid from.
    valid_from: Optional[datetime.datetime] = None
    # The DateTime that the Service containing this Route is valid until.
    valid_to: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl17:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl17
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl17()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "destination": lambda n : setattr(self, 'destination', n.get_str_value()),
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "originationName": lambda n : setattr(self, 'origination_name', n.get_str_value()),
            "originator": lambda n : setattr(self, 'originator', n.get_str_value()),
            "routeCode": lambda n : setattr(self, 'route_code', n.get_str_value()),
            "serviceType": lambda n : setattr(self, 'service_type', n.get_str_value()),
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
        writer.write_str_value("destination", self.destination)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("name", self.name)
        writer.write_str_value("originationName", self.origination_name)
        writer.write_str_value("originator", self.originator)
        writer.write_str_value("routeCode", self.route_code)
        writer.write_str_value("serviceType", self.service_type)
        writer.write_datetime_value("validFrom", self.valid_from)
        writer.write_datetime_value("validTo", self.valid_to)
        writer.write_additional_data_value(self.additional_data)
    

