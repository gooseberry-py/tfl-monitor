from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class FareTapDetails(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The busRouteId property
    bus_route_id: Optional[str] = None
    # The hostDeviceType property
    host_device_type: Optional[str] = None
    # The modeType property
    mode_type: Optional[str] = None
    # The nationalLocationCode property
    national_location_code: Optional[int] = None
    # The tapTimestamp property
    tap_timestamp: Optional[datetime.datetime] = None
    # The validationType property
    validation_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FareTapDetails:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FareTapDetails
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FareTapDetails()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "busRouteId": lambda n : setattr(self, 'bus_route_id', n.get_str_value()),
            "hostDeviceType": lambda n : setattr(self, 'host_device_type', n.get_str_value()),
            "modeType": lambda n : setattr(self, 'mode_type', n.get_str_value()),
            "nationalLocationCode": lambda n : setattr(self, 'national_location_code', n.get_int_value()),
            "tapTimestamp": lambda n : setattr(self, 'tap_timestamp', n.get_datetime_value()),
            "validationType": lambda n : setattr(self, 'validation_type', n.get_str_value()),
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
        writer.write_str_value("busRouteId", self.bus_route_id)
        writer.write_str_value("hostDeviceType", self.host_device_type)
        writer.write_str_value("modeType", self.mode_type)
        writer.write_int_value("nationalLocationCode", self.national_location_code)
        writer.write_datetime_value("tapTimestamp", self.tap_timestamp)
        writer.write_str_value("validationType", self.validation_type)
        writer.write_additional_data_value(self.additional_data)
    

