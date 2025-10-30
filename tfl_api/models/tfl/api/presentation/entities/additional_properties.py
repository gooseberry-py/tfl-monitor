from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class AdditionalProperties(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The category property
    category: Optional[str] = None
    # The key property
    key: Optional[str] = None
    # The modified property
    modified: Optional[datetime.datetime] = None
    # The sourceSystemKey property
    source_system_key: Optional[str] = None
    # The value property
    value: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> AdditionalProperties:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: AdditionalProperties
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return AdditionalProperties()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "key": lambda n : setattr(self, 'key', n.get_str_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_datetime_value()),
            "sourceSystemKey": lambda n : setattr(self, 'source_system_key', n.get_str_value()),
            "value": lambda n : setattr(self, 'value', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_str_value("key", self.key)
        writer.write_datetime_value("modified", self.modified)
        writer.write_str_value("sourceSystemKey", self.source_system_key)
        writer.write_str_value("value", self.value)
        writer.write_additional_data_value(self.additional_data)
    

