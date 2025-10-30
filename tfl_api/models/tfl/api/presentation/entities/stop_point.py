from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .additional_properties import AdditionalProperties
    from .identifier import Identifier
    from .line_group import LineGroup
    from .line_mode_group import LineModeGroup
    from .place import Place

@dataclass
class StopPoint(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The accessibilitySummary property
    accessibility_summary: Optional[str] = None
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
    # The fullName property
    full_name: Optional[str] = None
    # The hubNaptanCode property
    hub_naptan_code: Optional[str] = None
    # The icsCode property
    ics_code: Optional[str] = None
    # A unique identifier.
    id: Optional[str] = None
    # The indicator of the stop point e.g. "Stop K"
    indicator: Optional[str] = None
    # The individualStopId property
    individual_stop_id: Optional[str] = None
    # WGS84 latitude of the location.
    lat: Optional[float] = None
    # The lineGroup property
    line_group: Optional[list[LineGroup]] = None
    # The lineModeGroups property
    line_mode_groups: Optional[list[LineModeGroup]] = None
    # The lines property
    lines: Optional[list[Identifier]] = None
    # WGS84 longitude of the location.
    lon: Optional[float] = None
    # The modes property
    modes: Optional[list[str]] = None
    # The naptanId property
    naptan_id: Optional[str] = None
    # The naptanMode property
    naptan_mode: Optional[str] = None
    # The type of Place. See /Place/Meta/placeTypes for possible values.
    place_type: Optional[str] = None
    # The platformName property
    platform_name: Optional[str] = None
    # The smsCode property
    sms_code: Optional[str] = None
    # The stationNaptan property
    station_naptan: Optional[str] = None
    # The status property
    status: Optional[bool] = None
    # The stop letter, if it could be cleansed from the Indicator e.g. "K"
    stop_letter: Optional[str] = None
    # The stopType property
    stop_type: Optional[str] = None
    # The unique location of this resource.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StopPoint:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StopPoint
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StopPoint()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .additional_properties import AdditionalProperties
        from .identifier import Identifier
        from .line_group import LineGroup
        from .line_mode_group import LineModeGroup
        from .place import Place

        from .additional_properties import AdditionalProperties
        from .identifier import Identifier
        from .line_group import LineGroup
        from .line_mode_group import LineModeGroup
        from .place import Place

        fields: dict[str, Callable[[Any], None]] = {
            "accessibilitySummary": lambda n : setattr(self, 'accessibility_summary', n.get_str_value()),
            "additionalProperties": lambda n : setattr(self, 'additional_properties', n.get_collection_of_object_values(AdditionalProperties)),
            "children": lambda n : setattr(self, 'children', n.get_collection_of_object_values(Place)),
            "childrenUrls": lambda n : setattr(self, 'children_urls', n.get_collection_of_primitive_values(str)),
            "commonName": lambda n : setattr(self, 'common_name', n.get_str_value()),
            "distance": lambda n : setattr(self, 'distance', n.get_float_value()),
            "fullName": lambda n : setattr(self, 'full_name', n.get_str_value()),
            "hubNaptanCode": lambda n : setattr(self, 'hub_naptan_code', n.get_str_value()),
            "icsCode": lambda n : setattr(self, 'ics_code', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "indicator": lambda n : setattr(self, 'indicator', n.get_str_value()),
            "individualStopId": lambda n : setattr(self, 'individual_stop_id', n.get_str_value()),
            "lat": lambda n : setattr(self, 'lat', n.get_float_value()),
            "lineGroup": lambda n : setattr(self, 'line_group', n.get_collection_of_object_values(LineGroup)),
            "lineModeGroups": lambda n : setattr(self, 'line_mode_groups', n.get_collection_of_object_values(LineModeGroup)),
            "lines": lambda n : setattr(self, 'lines', n.get_collection_of_object_values(Identifier)),
            "lon": lambda n : setattr(self, 'lon', n.get_float_value()),
            "modes": lambda n : setattr(self, 'modes', n.get_collection_of_primitive_values(str)),
            "naptanId": lambda n : setattr(self, 'naptan_id', n.get_str_value()),
            "naptanMode": lambda n : setattr(self, 'naptan_mode', n.get_str_value()),
            "placeType": lambda n : setattr(self, 'place_type', n.get_str_value()),
            "platformName": lambda n : setattr(self, 'platform_name', n.get_str_value()),
            "smsCode": lambda n : setattr(self, 'sms_code', n.get_str_value()),
            "stationNaptan": lambda n : setattr(self, 'station_naptan', n.get_str_value()),
            "status": lambda n : setattr(self, 'status', n.get_bool_value()),
            "stopLetter": lambda n : setattr(self, 'stop_letter', n.get_str_value()),
            "stopType": lambda n : setattr(self, 'stop_type', n.get_str_value()),
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
        writer.write_str_value("accessibilitySummary", self.accessibility_summary)
        writer.write_collection_of_object_values("additionalProperties", self.additional_properties)
        writer.write_collection_of_object_values("children", self.children)
        writer.write_collection_of_primitive_values("childrenUrls", self.children_urls)
        writer.write_str_value("commonName", self.common_name)
        writer.write_float_value("distance", self.distance)
        writer.write_str_value("fullName", self.full_name)
        writer.write_str_value("hubNaptanCode", self.hub_naptan_code)
        writer.write_str_value("icsCode", self.ics_code)
        writer.write_str_value("id", self.id)
        writer.write_str_value("indicator", self.indicator)
        writer.write_str_value("individualStopId", self.individual_stop_id)
        writer.write_float_value("lat", self.lat)
        writer.write_collection_of_object_values("lineGroup", self.line_group)
        writer.write_collection_of_object_values("lineModeGroups", self.line_mode_groups)
        writer.write_collection_of_object_values("lines", self.lines)
        writer.write_float_value("lon", self.lon)
        writer.write_collection_of_primitive_values("modes", self.modes)
        writer.write_str_value("naptanId", self.naptan_id)
        writer.write_str_value("naptanMode", self.naptan_mode)
        writer.write_str_value("placeType", self.place_type)
        writer.write_str_value("platformName", self.platform_name)
        writer.write_str_value("smsCode", self.sms_code)
        writer.write_str_value("stationNaptan", self.station_naptan)
        writer.write_bool_value("status", self.status)
        writer.write_str_value("stopLetter", self.stop_letter)
        writer.write_str_value("stopType", self.stop_type)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

