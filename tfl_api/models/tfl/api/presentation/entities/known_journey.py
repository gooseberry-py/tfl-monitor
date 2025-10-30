from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class KnownJourney(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The hour property
    hour: Optional[str] = None
    # The intervalId property
    interval_id: Optional[int] = None
    # The minute property
    minute: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> KnownJourney:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: KnownJourney
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return KnownJourney()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "hour": lambda n : setattr(self, 'hour', n.get_str_value()),
            "intervalId": lambda n : setattr(self, 'interval_id', n.get_int_value()),
            "minute": lambda n : setattr(self, 'minute', n.get_str_value()),
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
        writer.write_str_value("hour", self.hour)
        writer.write_int_value("intervalId", self.interval_id)
        writer.write_str_value("minute", self.minute)
        writer.write_additional_data_value(self.additional_data)
    

