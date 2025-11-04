from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl20 import Tfl20
    from .tfl21 import Tfl21
    from .tfl22 import Tfl22

@dataclass
class Tfl23(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The direction property
    direction: Optional[str] = None
    # The isOutboundOnly property
    is_outbound_only: Optional[bool] = None
    # The lineId property
    line_id: Optional[str] = None
    # The lineName property
    line_name: Optional[str] = None
    # The lineStrings property
    line_strings: Optional[list[str]] = None
    # The mode property
    mode: Optional[str] = None
    # The orderedLineRoutes property
    ordered_line_routes: Optional[list[Tfl22]] = None
    # The stations property
    stations: Optional[list[Tfl20]] = None
    # The stopPointSequences property
    stop_point_sequences: Optional[list[Tfl21]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl23:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl23
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl23()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl20 import Tfl20
        from .tfl21 import Tfl21
        from .tfl22 import Tfl22

        from .tfl20 import Tfl20
        from .tfl21 import Tfl21
        from .tfl22 import Tfl22

        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "isOutboundOnly": lambda n : setattr(self, 'is_outbound_only', n.get_bool_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineName": lambda n : setattr(self, 'line_name', n.get_str_value()),
            "lineStrings": lambda n : setattr(self, 'line_strings', n.get_collection_of_primitive_values(str)),
            "mode": lambda n : setattr(self, 'mode', n.get_str_value()),
            "orderedLineRoutes": lambda n : setattr(self, 'ordered_line_routes', n.get_collection_of_object_values(Tfl22)),
            "stations": lambda n : setattr(self, 'stations', n.get_collection_of_object_values(Tfl20)),
            "stopPointSequences": lambda n : setattr(self, 'stop_point_sequences', n.get_collection_of_object_values(Tfl21)),
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
        writer.write_bool_value("isOutboundOnly", self.is_outbound_only)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineName", self.line_name)
        writer.write_collection_of_primitive_values("lineStrings", self.line_strings)
        writer.write_str_value("mode", self.mode)
        writer.write_collection_of_object_values("orderedLineRoutes", self.ordered_line_routes)
        writer.write_collection_of_object_values("stations", self.stations)
        writer.write_collection_of_object_values("stopPointSequences", self.stop_point_sequences)
        writer.write_additional_data_value(self.additional_data)
    

