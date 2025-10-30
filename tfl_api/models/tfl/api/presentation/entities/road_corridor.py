from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

@dataclass
class RoadCorridor(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The Bounds of the Corridor, given by the south-east followed by the north-west co-ordinate            pair in geoJSON format e.g. "[[-1.241531,51.242151],[1.641223,53.765721]]"
    bounds: Optional[str] = None
    # The display name of the Corridor e.g. "North Circular (A406)". This            may be identical to the Id.
    display_name: Optional[str] = None
    # The Envelope of the Corridor, given by the corner co-ordinates of a rectangular (four-point) polygon            in geoJSON format e.g. "[[-1.241531,51.242151],[-1.241531,53.765721],[1.641223,53.765721],[1.641223,51.242151]]"
    envelope: Optional[str] = None
    # The group name of the Corridor e.g. "Central London". Most corridors are not grouped, in which case this field can be null.
    group: Optional[str] = None
    # The Id of the Corridor e.g. "A406"
    id: Optional[str] = None
    # The end of the period over which status has been aggregated, or null if this is the current corridor status.
    status_aggregation_end_date: Optional[datetime.datetime] = None
    # The start of the period over which status has been aggregated, or null if this is the current corridor status.
    status_aggregation_start_date: Optional[datetime.datetime] = None
    # Standard multi-mode status severity code
    status_severity: Optional[str] = None
    # Description of the status severity as applied to RoadCorridors
    status_severity_description: Optional[str] = None
    # URL to retrieve this Corridor.
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoadCorridor:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoadCorridor
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoadCorridor()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        fields: dict[str, Callable[[Any], None]] = {
            "bounds": lambda n : setattr(self, 'bounds', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "envelope": lambda n : setattr(self, 'envelope', n.get_str_value()),
            "group": lambda n : setattr(self, 'group', n.get_str_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "statusAggregationEndDate": lambda n : setattr(self, 'status_aggregation_end_date', n.get_datetime_value()),
            "statusAggregationStartDate": lambda n : setattr(self, 'status_aggregation_start_date', n.get_datetime_value()),
            "statusSeverity": lambda n : setattr(self, 'status_severity', n.get_str_value()),
            "statusSeverityDescription": lambda n : setattr(self, 'status_severity_description', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("bounds", self.bounds)
        writer.write_str_value("displayName", self.display_name)
        writer.write_str_value("envelope", self.envelope)
        writer.write_str_value("group", self.group)
        writer.write_str_value("id", self.id)
        writer.write_datetime_value("statusAggregationEndDate", self.status_aggregation_end_date)
        writer.write_datetime_value("statusAggregationStartDate", self.status_aggregation_start_date)
        writer.write_str_value("statusSeverity", self.status_severity)
        writer.write_str_value("statusSeverityDescription", self.status_severity_description)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

