from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....system.data.spatial.db_geography import DbGeography

@dataclass
class RoadDisruptionLine(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The endDate property
    end_date: Optional[datetime.datetime] = None
    # The endTime property
    end_time: Optional[str] = None
    # The id property
    id: Optional[int] = None
    # The isDiversion property
    is_diversion: Optional[bool] = None
    # The multiLineString property
    multi_line_string: Optional[DbGeography] = None
    # The roadDisruptionId property
    road_disruption_id: Optional[str] = None
    # The startDate property
    start_date: Optional[datetime.datetime] = None
    # The startTime property
    start_time: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoadDisruptionLine:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoadDisruptionLine
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoadDisruptionLine()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....system.data.spatial.db_geography import DbGeography

        from .....system.data.spatial.db_geography import DbGeography

        fields: dict[str, Callable[[Any], None]] = {
            "endDate": lambda n : setattr(self, 'end_date', n.get_datetime_value()),
            "endTime": lambda n : setattr(self, 'end_time', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "isDiversion": lambda n : setattr(self, 'is_diversion', n.get_bool_value()),
            "multiLineString": lambda n : setattr(self, 'multi_line_string', n.get_object_value(DbGeography)),
            "roadDisruptionId": lambda n : setattr(self, 'road_disruption_id', n.get_str_value()),
            "startDate": lambda n : setattr(self, 'start_date', n.get_datetime_value()),
            "startTime": lambda n : setattr(self, 'start_time', n.get_str_value()),
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
        writer.write_datetime_value("endDate", self.end_date)
        writer.write_str_value("endTime", self.end_time)
        writer.write_int_value("id", self.id)
        writer.write_bool_value("isDiversion", self.is_diversion)
        writer.write_object_value("multiLineString", self.multi_line_string)
        writer.write_str_value("roadDisruptionId", self.road_disruption_id)
        writer.write_datetime_value("startDate", self.start_date)
        writer.write_str_value("startTime", self.start_time)
        writer.write_additional_data_value(self.additional_data)
    

