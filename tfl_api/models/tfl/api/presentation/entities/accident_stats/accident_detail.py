from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .casualty import Casualty
    from .vehicle import Vehicle

@dataclass
class AccidentDetail(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The borough property
    borough: Optional[str] = None
    # The casualties property
    casualties: Optional[list[Casualty]] = None
    # The date property
    date: Optional[datetime.datetime] = None
    # The id property
    id: Optional[int] = None
    # The lat property
    lat: Optional[float] = None
    # The location property
    location: Optional[str] = None
    # The lon property
    lon: Optional[float] = None
    # The severity property
    severity: Optional[str] = None
    # The vehicles property
    vehicles: Optional[list[Vehicle]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AccidentDetail:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AccidentDetail
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AccidentDetail()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .casualty import Casualty
        from .vehicle import Vehicle

        from .casualty import Casualty
        from .vehicle import Vehicle

        fields: dict[str, Callable[[Any], None]] = {
            "borough": lambda n : setattr(self, 'borough', n.get_str_value()),
            "casualties": lambda n : setattr(self, 'casualties', n.get_collection_of_object_values(Casualty)),
            "date": lambda n : setattr(self, 'date', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "lat": lambda n : setattr(self, 'lat', n.get_float_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "lon": lambda n : setattr(self, 'lon', n.get_float_value()),
            "severity": lambda n : setattr(self, 'severity', n.get_str_value()),
            "vehicles": lambda n : setattr(self, 'vehicles', n.get_collection_of_object_values(Vehicle)),
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
        writer.write_str_value("borough", self.borough)
        writer.write_collection_of_object_values("casualties", self.casualties)
        writer.write_datetime_value("date", self.date)
        writer.write_int_value("id", self.id)
        writer.write_float_value("lat", self.lat)
        writer.write_str_value("location", self.location)
        writer.write_float_value("lon", self.lon)
        writer.write_str_value("severity", self.severity)
        writer.write_collection_of_object_values("vehicles", self.vehicles)
        writer.write_additional_data_value(self.additional_data)
    

