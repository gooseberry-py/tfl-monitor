from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class DisruptedPoint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The additionalInformation property
    additional_information: Optional[str] = None
    # The appearance property
    appearance: Optional[str] = None
    # The atcoCode property
    atco_code: Optional[str] = None
    # The commonName property
    common_name: Optional[str] = None
    # The description property
    description: Optional[str] = None
    # The fromDate property
    from_date: Optional[datetime.datetime] = None
    # The mode property
    mode: Optional[str] = None
    # The stationAtcoCode property
    station_atco_code: Optional[str] = None
    # The toDate property
    to_date: Optional[datetime.datetime] = None
    # The type property
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> DisruptedPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: DisruptedPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return DisruptedPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "additionalInformation": lambda n : setattr(self, 'additional_information', n.get_str_value()),
            "appearance": lambda n : setattr(self, 'appearance', n.get_str_value()),
            "atcoCode": lambda n : setattr(self, 'atco_code', n.get_str_value()),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "fromDate": lambda n : setattr(self, 'from_date', n.get_datetime_value()),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "stationAtcoCode": lambda n : setattr(self, 'station_atco_code', n.get_str_value()),
            "toDate": lambda n : setattr(self, 'to_date', n.get_datetime_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("additionalInformation", self.additional_information)
        writer.write_str_value("appearance", self.appearance)
        writer.write_str_value("atcoCode", self.atco_code)
        writer.write_str_value("commonName", self.common_name)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("fromDate", self.from_date)
        writer.write_str_value("mode", self.mode)
        writer.write_str_value("stationAtcoCode", self.station_atco_code)
        writer.write_datetime_value("toDate", self.to_date)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

