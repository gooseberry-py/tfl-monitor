from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .identifier import Identifier

@dataclass
class MatchedStop(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The accessibilitySummary property
    accessibility_summary: Optional[str] = None
    # The direction property
    direction: Optional[str] = None
    # The hasDisruption property
    has_disruption: Optional[bool] = None
    # The icsId property
    ics_id: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The lat property
    lat: Optional[float] = None
    # The lines property
    lines: Optional[list[Identifier]] = None
    # The lon property
    lon: Optional[float] = None
    # The modes property
    modes: Optional[list[str]] = None
    # The name property
    name: Optional[str] = None
    # The parentId property
    parent_id: Optional[str] = None
    # The routeId property
    route_id: Optional[int] = None
    # The stationId property
    station_id: Optional[str] = None
    # The status property
    status: Optional[bool] = None
    # The stopLetter property
    stop_letter: Optional[str] = None
    # The stopType property
    stop_type: Optional[str] = None
    # The topMostParentId property
    top_most_parent_id: Optional[str] = None
    # The towards property
    towards: Optional[str] = None
    # The url property
    url: Optional[str] = None
    # The zone property
    zone: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> MatchedStop:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: MatchedStop
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return MatchedStop()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .identifier import Identifier

        from .identifier import Identifier

        fields: dict[str, Callable[[Any], None]] = {
            "accessibilitySummary": lambda n : setattr(self, 'accessibility_summary', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "hasDisruption": lambda n : setattr(self, 'has_disruption', n.get_bool_value()),
            "icsId": lambda n : setattr(self, 'ics_id', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lat": lambda n : setattr(self, 'lat', n.get_float_value()),
            "lines": lambda n : setattr(self, 'lines', n.get_collection_of_object_values(Identifier)),
            "lon": lambda n : setattr(self, 'lon', n.get_float_value()),
            "modes": lambda n : setattr(self, 'modes', n.get_collection_of_primitive_values(str)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "parentId": lambda n : setattr(self, 'parent_id', n.get_str_value()),
            "routeId": lambda n : setattr(self, 'route_id', n.get_int_value()),
            "stationId": lambda n : setattr(self, 'station_id', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_bool_value()),
            "stopLetter": lambda n : setattr(self, 'stop_letter', n.get_str_value()),
            "stopType": lambda n : setattr(self, 'stop_type', n.get_str_value()),
            "topMostParentId": lambda n : setattr(self, 'top_most_parent_id', n.get_str_value()),
            "towards": lambda n : setattr(self, 'towards', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
            "zone": lambda n : setattr(self, 'zone', n.get_str_value()),
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
        writer.write_str_value("accessibilitySummary", self.accessibility_summary)
        writer.write_str_value("direction", self.direction)
        writer.write_bool_value("hasDisruption", self.has_disruption)
        writer.write_str_value("icsId", self.ics_id)
        writer.write_str_value("id", self.id)
        writer.write_float_value("lat", self.lat)
        writer.write_collection_of_object_values("lines", self.lines)
        writer.write_float_value("lon", self.lon)
        writer.write_collection_of_primitive_values("modes", self.modes)
        writer.write_str_value("name", self.name)
        writer.write_str_value("parentId", self.parent_id)
        writer.write_int_value("routeId", self.route_id)
        writer.write_str_value("stationId", self.station_id)
        writer.write_bool_value("status", self.status)
        writer.write_str_value("stopLetter", self.stop_letter)
        writer.write_str_value("stopType", self.stop_type)
        writer.write_str_value("topMostParentId", self.top_most_parent_id)
        writer.write_str_value("towards", self.towards)
        writer.write_str_value("url", self.url)
        writer.write_str_value("zone", self.zone)
        writer.write_additional_data_value(self.additional_data)
    

