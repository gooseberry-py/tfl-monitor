from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl20 import Tfl20
    from .tfl24 import Tfl24
    from .tfl25 import Tfl25

@dataclass
class Tfl26(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The id property
    id: Optional[str] = None
    # The lat property
    lat: Optional[float] = None
    # The lineId property
    line_id: Optional[str] = None
    # The lineName property
    line_name: Optional[str] = None
    # The lineRouteSection property
    line_route_section: Optional[list[Tfl24]] = None
    # The lon property
    lon: Optional[float] = None
    # The matchedRouteSections property
    matched_route_sections: Optional[list[Tfl25]] = None
    # The matchedStops property
    matched_stops: Optional[list[Tfl20]] = None
    # The mode property
    mode: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The url property
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl26:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl26
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl26()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl20 import Tfl20
        from .tfl24 import Tfl24
        from .tfl25 import Tfl25

        from .tfl20 import Tfl20
        from .tfl24 import Tfl24
        from .tfl25 import Tfl25

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lat": lambda n : setattr(self, 'lat', n.get_float_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineName": lambda n : setattr(self, 'line_name', n.get_str_value()),
            "lineRouteSection": lambda n : setattr(self, 'line_route_section', n.get_collection_of_object_values(Tfl24)),
            "lon": lambda n : setattr(self, 'lon', n.get_float_value()),
            "matchedRouteSections": lambda n : setattr(self, 'matched_route_sections', n.get_collection_of_object_values(Tfl25)),
            "matchedStops": lambda n : setattr(self, 'matched_stops', n.get_collection_of_object_values(Tfl20)),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("id", self.id)
        writer.write_float_value("lat", self.lat)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineName", self.line_name)
        writer.write_collection_of_object_values("lineRouteSection", self.line_route_section)
        writer.write_float_value("lon", self.lon)
        writer.write_collection_of_object_values("matchedRouteSections", self.matched_route_sections)
        writer.write_collection_of_object_values("matchedStops", self.matched_stops)
        writer.write_str_value("mode", self.mode)
        writer.write_str_value("name", self.name)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

