from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl31 import Tfl31
    from .tfl32 import Tfl32
    from .tfl33_type import Tfl33_type

@dataclass
class Tfl33(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The frequency property
    frequency: Optional[Tfl32] = None
    # The fromTime property
    from_time: Optional[Tfl31] = None
    # The toTime property
    to_time: Optional[Tfl31] = None
    # The type property
    type: Optional[Tfl33_type] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl33:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl33
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl33()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl31 import Tfl31
        from .tfl32 import Tfl32
        from .tfl33_type import Tfl33_type

        from .tfl31 import Tfl31
        from .tfl32 import Tfl32
        from .tfl33_type import Tfl33_type

        fields: dict[str, Callable[[Any], None]] = {
            "frequency": lambda n : setattr(self, 'frequency', n.get_object_value(Tfl32)),
            "fromTime": lambda n : setattr(self, 'from_time', n.get_object_value(Tfl31)),
            "toTime": lambda n : setattr(self, 'to_time', n.get_object_value(Tfl31)),
            "type": lambda n : setattr(self, 'type', n.get_enum_value(Tfl33_type)),
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
        writer.write_object_value("frequency", self.frequency)
        writer.write_object_value("fromTime", self.from_time)
        writer.write_object_value("toTime", self.to_time)
        writer.write_enum_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

