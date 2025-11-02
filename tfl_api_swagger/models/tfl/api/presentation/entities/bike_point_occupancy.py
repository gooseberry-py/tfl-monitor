from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class BikePointOccupancy(AdditionalDataHolder, Parsable):
    """
    Bike point occupancy
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Total bike counts
    bikes_count: Optional[int] = None
    # Total ebikes count
    e_bikes_count: Optional[int] = None
    # Empty docks
    empty_docks: Optional[int] = None
    # Id of the bike point such as BikePoints_1
    id: Optional[str] = None
    # Name / Common name of the bike point
    name: Optional[str] = None
    # Total standard bikes count
    standard_bikes_count: Optional[int] = None
    # Total docks available
    total_docks: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> BikePointOccupancy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: BikePointOccupancy
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return BikePointOccupancy()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bikesCount": lambda n : setattr(self, 'bikes_count', n.get_int_value()),
            "eBikesCount": lambda n : setattr(self, 'e_bikes_count', n.get_int_value()),
            "emptyDocks": lambda n : setattr(self, 'empty_docks', n.get_int_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "standardBikesCount": lambda n : setattr(self, 'standard_bikes_count', n.get_int_value()),
            "totalDocks": lambda n : setattr(self, 'total_docks', n.get_int_value()),
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
        writer.write_int_value("bikesCount", self.bikes_count)
        writer.write_int_value("eBikesCount", self.e_bikes_count)
        writer.write_int_value("emptyDocks", self.empty_docks)
        writer.write_str_value("id", self.id)
        writer.write_str_value("name", self.name)
        writer.write_int_value("standardBikesCount", self.standard_bikes_count)
        writer.write_int_value("totalDocks", self.total_docks)
        writer.write_additional_data_value(self.additional_data)
    

