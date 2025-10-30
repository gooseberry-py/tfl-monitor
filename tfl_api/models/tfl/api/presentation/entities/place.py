from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_properties import AdditionalProperties

@dataclass
class Place(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # A bag of additional key/value pairs with extra information about this place.
    additional_properties: Optional[list[AdditionalProperties]] = None
    # The children property
    children: Optional[list[Place]] = None
    # The childrenUrls property
    children_urls: Optional[list[str]] = None
    # A human readable name.
    common_name: Optional[str] = None
    # The distance of the place from its search point, if this is the result            of a geographical search, otherwise zero.
    distance: Optional[float] = None
    # A unique identifier.
    id: Optional[str] = None
    # WGS84 latitude of the location.
    lat: Optional[float] = None
    # WGS84 longitude of the location.
    lon: Optional[float] = None
    # The type of Place. See /Place/Meta/placeTypes for possible values.
    place_type: Optional[str] = None
    # The unique location of this resource.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Place:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Place
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Place()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .additional_properties import AdditionalProperties

        from .additional_properties import AdditionalProperties

        fields: dict[str, Callable[[Any], None]] = {
            "additionalProperties": lambda n : setattr(self, 'additional_properties', n.get_collection_of_object_values(AdditionalProperties)),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(Place)),
            "childrenUrls": lambda n : setattr(self, 'children_urls', n.get_collection_of_primitive_values(str)),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "distance": lambda n : setattr(self, 'distance', n.get_float_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lat": lambda n : setattr(self, 'lat', n.get_float_value()),
            "lon": lambda n : setattr(self, 'lon', n.get_float_value()),
            "placeType": lambda n : setattr(self, 'place_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("additionalProperties", self.additional_properties)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_collection_of_primitive_values("childrenUrls", self.children_urls)
        writer.write_str_value("commonName", self.common_name)
        writer.write_float_value("distance", self.distance)
        writer.write_str_value("id", self.id)
        writer.write_float_value("lat", self.lat)
        writer.write_float_value("lon", self.lon)
        writer.write_str_value("placeType", self.place_type)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

