from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .crowding import Crowding
    from .identifier_route_type import Identifier_routeType
    from .identifier_status import Identifier_status

@dataclass
class Identifier(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The crowding property
    crowding: Optional[Crowding] = None
    # The fullName property
    full_name: Optional[str] = None
    # The id property
    id: Optional[str] = None
    # The motType property
    mot_type: Optional[str] = None
    # The name property
    name: Optional[str] = None
    # The network property
    network: Optional[str] = None
    # The routeType property
    route_type: Optional[Identifier_routeType] = None
    # The status property
    status: Optional[Identifier_status] = None
    # The type property
    type: Optional[str] = None
    # The uri property
    uri: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Identifier:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Identifier
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Identifier()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .crowding import Crowding
        from .identifier_route_type import Identifier_routeType
        from .identifier_status import Identifier_status

        from .crowding import Crowding
        from .identifier_route_type import Identifier_routeType
        from .identifier_status import Identifier_status

        fields: dict[str, Callable[[Any], None]] = {
            "crowding": lambda n : setattr(self, 'crowding', n.get_object_value(Crowding)),
            "fullName": lambda n : setattr(self, 'full_name', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "motType": lambda n : setattr(self, 'mot_type', n.get_str_value()),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "network": lambda n : setattr(self, 'network', n.get_str_value()),
            "routeType": lambda n : setattr(self, 'route_type', n.get_enum_value(Identifier_routeType)),
            "status": lambda n : setattr(self, 'status', n.get_enum_value(Identifier_status)),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
            "uri": lambda n : setattr(self, 'uri', n.get_str_value()),
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
        writer.write_object_value("crowding", self.crowding)
        writer.write_str_value("fullName", self.full_name)
        writer.write_str_value("id", self.id)
        writer.write_str_value("motType", self.mot_type)
        writer.write_str_value("name", self.name)
        writer.write_str_value("network", self.network)
        writer.write_enum_value("routeType", self.route_type)
        writer.write_enum_value("status", self.status)
        writer.write_str_value("type", self.type)
        writer.write_str_value("uri", self.uri)
        writer.write_additional_data_value(self.additional_data)
    

