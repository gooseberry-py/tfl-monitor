from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .disruption import Disruption
    from .validity_period import ValidityPeriod

@dataclass
class LineStatus(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The created property
    created: Optional[datetime.datetime] = None
    # Represents a disruption to a route within the transport network.
    disruption: Optional[Disruption] = None
    # The id property
    id: Optional[int] = None
    # The lineId property
    line_id: Optional[str] = None
    # The modified property
    modified: Optional[datetime.datetime] = None
    # The reason property
    reason: Optional[str] = None
    # The statusSeverity property
    status_severity: Optional[int] = None
    # The statusSeverityDescription property
    status_severity_description: Optional[str] = None
    # The validityPeriods property
    validity_periods: Optional[list[ValidityPeriod]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> LineStatus:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: LineStatus
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return LineStatus()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .disruption import Disruption
        from .validity_period import ValidityPeriod

        from .disruption import Disruption
        from .validity_period import ValidityPeriod

        fields: dict[str, Callable[[Any], None]] = {
            "created": lambda n : setattr(self, 'created', n.get_datetime_value()),
            "disruption": lambda n : setattr(self, 'disruption', n.get_object_value(Disruption)),
            "id": lambda n : setattr(self, 'id', n.get_int_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "modified": lambda n : setattr(self, 'modified', n.get_datetime_value()),
            "reason": lambda n : setattr(self, 'reason', n.get_str_value()),
            "statusSeverity": lambda n : setattr(self, 'status_severity', n.get_int_value()),
            "statusSeverityDescription": lambda n : setattr(self, 'status_severity_description', n.get_str_value()),
            "validityPeriods": lambda n : setattr(self, 'validity_periods', n.get_collection_of_object_values(ValidityPeriod)),
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
        writer.write_datetime_value("created", self.created)
        writer.write_object_value("disruption", self.disruption)
        writer.write_int_value("id", self.id)
        writer.write_str_value("lineId", self.line_id)
        writer.write_datetime_value("modified", self.modified)
        writer.write_str_value("reason", self.reason)
        writer.write_int_value("statusSeverity", self.status_severity)
        writer.write_str_value("statusSeverityDescription", self.status_severity_description)
        writer.write_collection_of_object_values("validityPeriods", self.validity_periods)
        writer.write_additional_data_value(self.additional_data)
    

