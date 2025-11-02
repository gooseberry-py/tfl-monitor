from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .time_adjustment import TimeAdjustment

@dataclass
class TimeAdjustments(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The earlier property
    earlier: Optional[TimeAdjustment] = None
    # The earliest property
    earliest: Optional[TimeAdjustment] = None
    # The later property
    later: Optional[TimeAdjustment] = None
    # The latest property
    latest: Optional[TimeAdjustment] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> TimeAdjustments:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: TimeAdjustments
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return TimeAdjustments()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .time_adjustment import TimeAdjustment

        from .time_adjustment import TimeAdjustment

        fields: dict[str, Callable[[Any], None]] = {
            "earlier": lambda n : setattr(self, 'earlier', n.get_object_value(TimeAdjustment)),
            "earliest": lambda n : setattr(self, 'earliest', n.get_object_value(TimeAdjustment)),
            "later": lambda n : setattr(self, 'later', n.get_object_value(TimeAdjustment)),
            "latest": lambda n : setattr(self, 'latest', n.get_object_value(TimeAdjustment)),
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
        writer.write_object_value("earlier", self.earlier)
        writer.write_object_value("earliest", self.earliest)
        writer.write_object_value("later", self.later)
        writer.write_object_value("latest", self.latest)
        writer.write_additional_data_value(self.additional_data)
    

