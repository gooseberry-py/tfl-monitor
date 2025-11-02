from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .line_specific_service_type import LineSpecificServiceType

@dataclass
class LineServiceType(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The lineName property
    line_name: Optional[str] = None
    # The lineSpecificServiceTypes property
    line_specific_service_types: Optional[list[LineSpecificServiceType]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LineServiceType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LineServiceType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LineServiceType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .line_specific_service_type import LineSpecificServiceType

        from .line_specific_service_type import LineSpecificServiceType

        fields: dict[str, Callable[[Any], None]] = {
            "lineName": lambda n : setattr(self, 'line_name', n.get_str_value()),
            "lineSpecificServiceTypes": lambda n : setattr(self, 'line_specific_service_types', n.get_collection_of_object_values(LineSpecificServiceType)),
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
        writer.write_str_value("lineName", self.line_name)
        writer.write_collection_of_object_values("lineSpecificServiceTypes", self.line_specific_service_types)
        writer.write_additional_data_value(self.additional_data)
    

