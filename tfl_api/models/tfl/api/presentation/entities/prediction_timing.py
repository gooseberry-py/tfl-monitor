from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class PredictionTiming(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The countdownServerAdjustment property
    countdown_server_adjustment: Optional[str] = None
    # The insert property
    insert: Optional[datetime.datetime] = None
    # The read property
    read: Optional[datetime.datetime] = None
    # The received property
    received: Optional[datetime.datetime] = None
    # The sent property
    sent: Optional[datetime.datetime] = None
    # The source property
    source: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> PredictionTiming:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: PredictionTiming
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return PredictionTiming()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "countdownServerAdjustment": lambda n : setattr(self, 'countdown_server_adjustment', n.get_str_value()),
            "insert": lambda n : setattr(self, 'insert', n.get_datetime_value()),
            "read": lambda n : setattr(self, 'read', n.get_datetime_value()),
            "received": lambda n : setattr(self, 'received', n.get_datetime_value()),
            "sent": lambda n : setattr(self, 'sent', n.get_datetime_value()),
            "source": lambda n : setattr(self, 'source', n.get_datetime_value()),
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
        writer.write_str_value("countdownServerAdjustment", self.countdown_server_adjustment)
        writer.write_datetime_value("insert", self.insert)
        writer.write_datetime_value("read", self.read)
        writer.write_datetime_value("received", self.received)
        writer.write_datetime_value("sent", self.sent)
        writer.write_datetime_value("source", self.source)
        writer.write_additional_data_value(self.additional_data)
    

