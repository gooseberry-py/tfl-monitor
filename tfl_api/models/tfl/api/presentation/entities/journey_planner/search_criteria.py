from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .search_criteria_date_time_type import SearchCriteria_dateTimeType
    from .time_adjustments import TimeAdjustments

@dataclass
class SearchCriteria(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The dateTime property
    date_time: Optional[datetime.datetime] = None
    # The dateTimeType property
    date_time_type: Optional[SearchCriteria_dateTimeType] = None
    # The timeAdjustments property
    time_adjustments: Optional[TimeAdjustments] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> SearchCriteria:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: SearchCriteria
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return SearchCriteria()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .search_criteria_date_time_type import SearchCriteria_dateTimeType
        from .time_adjustments import TimeAdjustments

        from .search_criteria_date_time_type import SearchCriteria_dateTimeType
        from .time_adjustments import TimeAdjustments

        fields: dict[str, Callable[[Any], None]] = {
            "dateTime": lambda n : setattr(self, 'date_time', n.get_datetime_value()),
            "dateTimeType": lambda n : setattr(self, 'date_time_type', n.get_enum_value(SearchCriteria_dateTimeType)),
            "timeAdjustments": lambda n : setattr(self, 'time_adjustments', n.get_object_value(TimeAdjustments)),
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
        writer.write_datetime_value("dateTime", self.date_time)
        writer.write_enum_value("dateTimeType", self.date_time_type)
        writer.write_object_value("timeAdjustments", self.time_adjustments)
        writer.write_additional_data_value(self.additional_data)
    

