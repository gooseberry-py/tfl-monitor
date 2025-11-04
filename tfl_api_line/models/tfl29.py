from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl28 import Tfl28

@dataclass
class Tfl29(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The id property
    id: Optional[str] = None
    # The intervals property
    intervals: Optional[list[Tfl28]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl29:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl29
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl29()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl28 import Tfl28

        from .tfl28 import Tfl28

        fields: dict[str, Callable[[Any], None]] = {
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "intervals": lambda n : setattr(self, 'intervals', n.get_collection_of_object_values(Tfl28)),
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
        writer.write_collection_of_object_values("intervals", self.intervals)
        writer.write_additional_data_value(self.additional_data)
    

