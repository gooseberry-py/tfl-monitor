from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .instruction_step import InstructionStep

@dataclass
class Instruction(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The detailed property
    detailed: Optional[str] = None
    # The steps property
    steps: Optional[list[InstructionStep]] = None
    # The summary property
    summary: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Instruction:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Instruction
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Instruction()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .instruction_step import InstructionStep

        from .instruction_step import InstructionStep

        fields: dict[str, Callable[[Any], None]] = {
            "detailed": lambda n : setattr(self, 'detailed', n.get_str_value()),
            "steps": lambda n : setattr(self, 'steps', n.get_collection_of_object_values(InstructionStep)),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
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
        writer.write_str_value("detailed", self.detailed)
        writer.write_collection_of_object_values("steps", self.steps)
        writer.write_str_value("summary", self.summary)
        writer.write_additional_data_value(self.additional_data)
    

