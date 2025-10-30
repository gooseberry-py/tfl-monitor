from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ....common.journey_planner.jp_elevation import JpElevation
    from ..identifier import Identifier

@dataclass
class Path(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The elevation property
    elevation: Optional[list[JpElevation]] = None
    # The lineString property
    line_string: Optional[str] = None
    # The stopPoints property
    stop_points: Optional[list[Identifier]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Path:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Path
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Path()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from ....common.journey_planner.jp_elevation import JpElevation
        from ..identifier import Identifier

        from ....common.journey_planner.jp_elevation import JpElevation
        from ..identifier import Identifier

        fields: dict[str, Callable[[Any], None]] = {
            "elevation": lambda n : setattr(self, 'elevation', n.get_collection_of_object_values(JpElevation)),
            "lineString": lambda n : setattr(self, 'line_string', n.get_str_value()),
            "stopPoints": lambda n : setattr(self, 'stop_points', n.get_collection_of_object_values(Identifier)),
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
        writer.write_collection_of_object_values("elevation", self.elevation)
        writer.write_str_value("lineString", self.line_string)
        writer.write_collection_of_object_values("stopPoints", self.stop_points)
        writer.write_additional_data_value(self.additional_data)
    

