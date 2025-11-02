from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .crowding import Crowding
    from .disruption import Disruption
    from .line_service_type_info import LineServiceTypeInfo
    from .line_status import LineStatus
    from .matched_route import MatchedRoute

@dataclass
class Line(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created property
    created: Optional[datetime.datetime] = None
    # The crowding property
    crowding: Optional[Crowding] = None
    # The disruptions property
    disruptions: Optional[list[Disruption]] = None
    # The id property
    id: Optional[str] = None
    # The lineStatuses property
    line_statuses: Optional[list[LineStatus]] = None
    # The modeName property
    mode_name: Optional[str] = None
    # The modified property
    modified: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The routeSections property
    route_sections: Optional[list[MatchedRoute]] = None
    # The serviceTypes property
    service_types: Optional[list[LineServiceTypeInfo]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Line:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Line
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Line()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .crowding import Crowding
        from .disruption import Disruption
        from .line_service_type_info import LineServiceTypeInfo
        from .line_status import LineStatus
        from .matched_route import MatchedRoute

        from .crowding import Crowding
        from .disruption import Disruption
        from .line_service_type_info import LineServiceTypeInfo
        from .line_status import LineStatus
        from .matched_route import MatchedRoute

        fields: dict[str, Callable[[Any], None]] = {
            "created": lambda n : setattr(self, 'created', n.get_datetime_value()),
            "crowding": lambda n : setattr(self, 'crowding', n.get_object_value(Crowding)),
            "disruptions": lambda n : setattr(self, 'disruptions', n.get_collection_of_object_values(Disruption)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lineStatuses": lambda n : setattr(self, 'line_statuses', n.get_collection_of_object_values(LineStatus)),
            "modeName": lambda n : setattr(self, 'mode_name', n.get_str_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "routeSections": lambda n : setattr(self, 'route_sections', n.get_collection_of_object_values(MatchedRoute)),
            "serviceTypes": lambda n : setattr(self, 'service_types', n.get_collection_of_object_values(LineServiceTypeInfo)),
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
        writer.write_datetime_value("created", self.created)
        writer.write_object_value("crowding", self.crowding)
        writer.write_collection_of_object_values("disruptions", self.disruptions)
        writer.write_str_value("id", self.id)
        writer.write_collection_of_object_values("lineStatuses", self.line_statuses)
        writer.write_str_value("modeName", self.mode_name)
        writer.write_datetime_value("modified", self.modified)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("routeSections", self.route_sections)
        writer.write_collection_of_object_values("serviceTypes", self.service_types)
        writer.write_additional_data_value(self.additional_data)
    

