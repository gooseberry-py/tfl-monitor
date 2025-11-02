from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ..identifier import Identifier

@dataclass
class RouteOption(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The direction of the route, i.e. outbound or inbound.
    direction: Optional[str] = None
    # The directions property
    directions: Optional[list[str]] = None
    # The Id of the route
    id: Optional[str] = None
    # The lineIdentifier property
    line_identifier: Optional[Identifier] = None
    # Name such as "72"
    name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RouteOption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RouteOption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RouteOption()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ..identifier import Identifier

        from ..identifier import Identifier

        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "directions": lambda n : setattr(self, 'directions', n.get_collection_of_primitive_values(str)),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lineIdentifier": lambda n : setattr(self, 'line_identifier', n.get_object_value(Identifier)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
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
        writer.write_str_value("direction", self.direction)
        writer.write_collection_of_primitive_values("directions", self.directions)
        writer.write_str_value("id", self.id)
        writer.write_object_value("lineIdentifier", self.line_identifier)
        writer.write_str_value("name", self.name)
        writer.write_additional_data_value(self.additional_data)
    

