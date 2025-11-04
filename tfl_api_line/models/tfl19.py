from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl14 import Tfl14
    from .tfl16 import Tfl16
    from .tfl17 import Tfl17
    from .tfl18 import Tfl18
    from .tfl5 import Tfl5

@dataclass
class Tfl19(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created property
    created: Optional[datetime.datetime] = None
    # The crowding property
    crowding: Optional[Tfl5] = None
    # The disruptions property
    disruptions: Optional[list[Tfl14]] = None
    # The id property
    id: Optional[str] = None
    # The lineStatuses property
    line_statuses: Optional[list[Tfl16]] = None
    # The modeName property
    mode_name: Optional[str] = None
    # The modified property
    modified: Optional[datetime.datetime] = None
    # The name property
    name: Optional[str] = None
    # The routeSections property
    route_sections: Optional[list[Tfl17]] = None
    # The serviceTypes property
    service_types: Optional[list[Tfl18]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl19:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl19
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl19()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl14 import Tfl14
        from .tfl16 import Tfl16
        from .tfl17 import Tfl17
        from .tfl18 import Tfl18
        from .tfl5 import Tfl5

        from .tfl14 import Tfl14
        from .tfl16 import Tfl16
        from .tfl17 import Tfl17
        from .tfl18 import Tfl18
        from .tfl5 import Tfl5

        fields: dict[str, Callable[[Any], None]] = {
            "created": lambda n : setattr(self, 'created', n.get_datetime_value()),
            "crowding": lambda n : setattr(self, 'crowding', n.get_object_value(Tfl5)),
            "disruptions": lambda n : setattr(self, 'disruptions', n.get_collection_of_object_values(Tfl14)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lineStatuses": lambda n : setattr(self, 'line_statuses', n.get_collection_of_object_values(Tfl16)),
            "modeName": lambda n : setattr(self, 'mode_name', n.get_str_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_datetime_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "routeSections": lambda n : setattr(self, 'route_sections', n.get_collection_of_object_values(Tfl17)),
            "serviceTypes": lambda n : setattr(self, 'service_types', n.get_collection_of_object_values(Tfl18)),
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
    

