from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .arrival_departure_departure_status import ArrivalDeparture_departureStatus
    from .prediction_timing import PredictionTiming

@dataclass
class ArrivalDeparture(AdditionalDataHolder, Parsable):
    """
    DTO to capture the prediction details
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Reason for cancellation or delay
    cause: Optional[str] = None
    # Status of departure
    departure_status: Optional[ArrivalDeparture_departureStatus] = None
    # Name of the destination
    destination_name: Optional[str] = None
    # Naptan Identifier for the prediction's destination
    destination_naptan_id: Optional[str] = None
    # Estimated time of arrival
    estimated_time_of_arrival: Optional[datetime.datetime] = None
    # Estimated time of arrival
    estimated_time_of_departure: Optional[datetime.datetime] = None
    # Estimated time of arrival
    minutes_and_seconds_to_arrival: Optional[str] = None
    # Estimated time of arrival
    minutes_and_seconds_to_departure: Optional[str] = None
    # Identifier for the prediction
    naptan_id: Optional[str] = None
    # Platform name (for bus, this is the stop letter)
    platform_name: Optional[str] = None
    # Estimated time of arrival
    scheduled_time_of_arrival: Optional[datetime.datetime] = None
    # Estimated time of arrival
    scheduled_time_of_departure: Optional[datetime.datetime] = None
    # Station name
    station_name: Optional[str] = None
    # The timing property
    timing: Optional[PredictionTiming] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> ArrivalDeparture:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: ArrivalDeparture
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return ArrivalDeparture()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .arrival_departure_departure_status import ArrivalDeparture_departureStatus
        from .prediction_timing import PredictionTiming

        from .arrival_departure_departure_status import ArrivalDeparture_departureStatus
        from .prediction_timing import PredictionTiming

        fields: dict[str, Callable[[Any], None]] = {
            "cause": lambda n : setattr(self, 'cause', n.get_str_value()),
            "departureStatus": lambda n : setattr(self, 'departure_status', n.get_enum_value(ArrivalDeparture_departureStatus)),
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "destinationNaptanId": lambda n : setattr(self, 'destination_naptan_id', n.get_str_value()),
            "estimatedTimeOfArrival": lambda n : setattr(self, 'estimated_time_of_arrival', n.get_datetime_value()),
            "estimatedTimeOfDeparture": lambda n : setattr(self, 'estimated_time_of_departure', n.get_datetime_value()),
            "minutesAndSecondsToArrival": lambda n : setattr(self, 'minutes_and_seconds_to_arrival', n.get_str_value()),
            "minutesAndSecondsToDeparture": lambda n : setattr(self, 'minutes_and_seconds_to_departure', n.get_str_value()),
            "naptanId": lambda n : setattr(self, 'naptan_id', n.get_str_value()),
            "platformName": lambda n : setattr(self, 'platform_name', n.get_str_value()),
            "scheduledTimeOfArrival": lambda n : setattr(self, 'scheduled_time_of_arrival', n.get_datetime_value()),
            "scheduledTimeOfDeparture": lambda n : setattr(self, 'scheduled_time_of_departure', n.get_datetime_value()),
            "stationName": lambda n : setattr(self, 'station_name', n.get_str_value()),
            "timing": lambda n : setattr(self, 'timing', n.get_object_value(PredictionTiming)),
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
        writer.write_str_value("cause", self.cause)
        writer.write_enum_value("departureStatus", self.departure_status)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_str_value("destinationNaptanId", self.destination_naptan_id)
        writer.write_datetime_value("estimatedTimeOfArrival", self.estimated_time_of_arrival)
        writer.write_datetime_value("estimatedTimeOfDeparture", self.estimated_time_of_departure)
        writer.write_str_value("minutesAndSecondsToArrival", self.minutes_and_seconds_to_arrival)
        writer.write_str_value("minutesAndSecondsToDeparture", self.minutes_and_seconds_to_departure)
        writer.write_str_value("naptanId", self.naptan_id)
        writer.write_str_value("platformName", self.platform_name)
        writer.write_datetime_value("scheduledTimeOfArrival", self.scheduled_time_of_arrival)
        writer.write_datetime_value("scheduledTimeOfDeparture", self.scheduled_time_of_departure)
        writer.write_str_value("stationName", self.station_name)
        writer.write_object_value("timing", self.timing)
        writer.write_additional_data_value(self.additional_data)
    

