from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fare_tap_details import FareTapDetails

@dataclass
class FareTap(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The atcoCode property
    atco_code: Optional[str] = None
    # The tapDetails property
    tap_details: Optional[FareTapDetails] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> FareTap:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: FareTap
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return FareTap()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fare_tap_details import FareTapDetails

        from .fare_tap_details import FareTapDetails

        fields: dict[str, Callable[[Any], None]] = {
            "atcoCode": lambda n : setattr(self, 'atco_code', n.get_str_value()),
            "tapDetails": lambda n : setattr(self, 'tap_details', n.get_object_value(FareTapDetails)),
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
        writer.write_str_value("atcoCode", self.atco_code)
        writer.write_object_value("tapDetails", self.tap_details)
        writer.write_additional_data_value(self.additional_data)
    

