from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class Tfl15(AdditionalDataHolder, Parsable):
    """
    Represents a period for which a planned works is valid.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Gets or sets the start date.
    from_date: Optional[datetime.datetime] = None
    # If true is a realtime status rather than planned or info
    is_now: Optional[bool] = None
    # Gets or sets the end date.
    to_date: Optional[datetime.datetime] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl15:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl15
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl15()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "fromDate": lambda n : setattr(self, 'from_date', n.get_datetime_value()),
            "isNow": lambda n : setattr(self, 'is_now', n.get_bool_value()),
            "toDate": lambda n : setattr(self, 'to_date', n.get_datetime_value()),
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
        writer.write_datetime_value("fromDate", self.from_date)
        writer.write_bool_value("isNow", self.is_now)
        writer.write_datetime_value("toDate", self.to_date)
        writer.write_additional_data_value(self.additional_data)
    

