from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .line_service_type_info import LineServiceTypeInfo

@dataclass
class LineSpecificServiceType(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The serviceType property
    service_type: Optional[LineServiceTypeInfo] = None
    # The stopServesServiceType property
    stop_serves_service_type: Optional[bool] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LineSpecificServiceType:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LineSpecificServiceType
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LineSpecificServiceType()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .line_service_type_info import LineServiceTypeInfo

        from .line_service_type_info import LineServiceTypeInfo

        fields: dict[str, Callable[[Any], None]] = {
            "serviceType": lambda n : setattr(self, 'service_type', n.get_object_value(LineServiceTypeInfo)),
            "stopServesServiceType": lambda n : setattr(self, 'stop_serves_service_type', n.get_bool_value()),
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
        writer.write_object_value("serviceType", self.service_type)
        writer.write_bool_value("stopServesServiceType", self.stop_serves_service_type)
        writer.write_additional_data_value(self.additional_data)
    

