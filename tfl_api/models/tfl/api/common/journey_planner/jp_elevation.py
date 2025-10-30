from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class JpElevation(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The distance property
    distance: Optional[int] = None
    # The endLat property
    end_lat: Optional[float] = None
    # The endLon property
    end_lon: Optional[float] = None
    # The gradient property
    gradient: Optional[float] = None
    # The heightFromPreviousPoint property
    height_from_previous_point: Optional[int] = None
    # The startElevation property
    start_elevation: Optional[int] = None
    # The startLat property
    start_lat: Optional[float] = None
    # The startLon property
    start_lon: Optional[float] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JpElevation:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JpElevation
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JpElevation()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "distance": lambda n : setattr(self, 'distance', n.get_int_value()),
            "endLat": lambda n : setattr(self, 'end_lat', n.get_float_value()),
            "endLon": lambda n : setattr(self, 'end_lon', n.get_float_value()),
            "gradient": lambda n : setattr(self, 'gradient', n.get_float_value()),
            "heightFromPreviousPoint": lambda n : setattr(self, 'height_from_previous_point', n.get_int_value()),
            "startElevation": lambda n : setattr(self, 'start_elevation', n.get_int_value()),
            "startLat": lambda n : setattr(self, 'start_lat', n.get_float_value()),
            "startLon": lambda n : setattr(self, 'start_lon', n.get_float_value()),
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
        writer.write_int_value("distance", self.distance)
        writer.write_float_value("endLat", self.end_lat)
        writer.write_float_value("endLon", self.end_lon)
        writer.write_float_value("gradient", self.gradient)
        writer.write_int_value("heightFromPreviousPoint", self.height_from_previous_point)
        writer.write_int_value("startElevation", self.start_elevation)
        writer.write_float_value("startLat", self.start_lat)
        writer.write_float_value("startLon", self.start_lon)
        writer.write_additional_data_value(self.additional_data)
    

