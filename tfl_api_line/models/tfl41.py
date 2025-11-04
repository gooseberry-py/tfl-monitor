from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl40 import Tfl40

@dataclass
class Tfl41(AdditionalDataHolder, Parsable):
    """
    DTO to capture the prediction details
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Bearing (between 0 to 359)
    bearing: Optional[str] = None
    # The current location of the vehicle.
    current_location: Optional[str] = None
    # Name of the destination
    destination_name: Optional[str] = None
    # Naptan Identifier for the prediction's destination
    destination_naptan_id: Optional[str] = None
    # Direction (unified to inbound/outbound)
    direction: Optional[str] = None
    # The expected arrival time of the vehicle at the stop/station
    expected_arrival: Optional[datetime.datetime] = None
    # The identitier for the prediction
    id: Optional[str] = None
    # Unique identifier for the Line
    line_id: Optional[str] = None
    # Line Name
    line_name: Optional[str] = None
    # The mode name of the station/line the prediction relates to
    mode_name: Optional[str] = None
    # Identifier for the prediction
    naptan_id: Optional[str] = None
    # The type of the operation (1: is new or has been updated, 2: should be deleted from any client cache)
    operation_type: Optional[int] = None
    # Platform name (for bus, this is the stop letter)
    platform_name: Optional[str] = None
    # Station name
    station_name: Optional[str] = None
    # The expiry time for the prediction
    time_to_live: Optional[datetime.datetime] = None
    # Prediction of the Time to station in seconds
    time_to_station: Optional[int] = None
    # Timestamp for when the prediction was inserted/modified (source column drives what objects are broadcast on each iteration)
    timestamp: Optional[datetime.datetime] = None
    # The timing property
    timing: Optional[Tfl40] = None
    # Routing information or other descriptive text about the path of the vehicle towards the destination
    towards: Optional[str] = None
    # The actual vehicle in transit (for train modes, the leading car of the rolling set)
    vehicle_id: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl41:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl41
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl41()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl40 import Tfl40

        from .tfl40 import Tfl40

        fields: dict[str, Callable[[Any], None]] = {
            "bearing": lambda n : setattr(self, 'bearing', n.get_str_value()),
            "currentLocation": lambda n : setattr(self, 'current_location', n.get_str_value()),
            "destinationName": lambda n : setattr(self, 'destination_name', n.get_str_value()),
            "destinationNaptanId": lambda n : setattr(self, 'destination_naptan_id', n.get_str_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "expectedArrival": lambda n : setattr(self, 'expected_arrival', n.get_datetime_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineName": lambda n : setattr(self, 'line_name', n.get_str_value()),
            "modeName": lambda n : setattr(self, 'mode_name', n.get_str_value()),
            "naptanId": lambda n : setattr(self, 'naptan_id', n.get_str_value()),
            "operationType": lambda n : setattr(self, 'operation_type', n.get_int_value()),
            "platformName": lambda n : setattr(self, 'platform_name', n.get_str_value()),
            "stationName": lambda n : setattr(self, 'station_name', n.get_str_value()),
            "timeToLive": lambda n : setattr(self, 'time_to_live', n.get_datetime_value()),
            "timeToStation": lambda n : setattr(self, 'time_to_station', n.get_int_value()),
            "timestamp": lambda n : setattr(self, 'timestamp', n.get_datetime_value()),
            "timing": lambda n : setattr(self, 'timing', n.get_object_value(Tfl40)),
            "towards": lambda n : setattr(self, 'towards', n.get_str_value()),
            "vehicleId": lambda n : setattr(self, 'vehicle_id', n.get_str_value()),
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
        writer.write_str_value("bearing", self.bearing)
        writer.write_str_value("currentLocation", self.current_location)
        writer.write_str_value("destinationName", self.destination_name)
        writer.write_str_value("destinationNaptanId", self.destination_naptan_id)
        writer.write_str_value("direction", self.direction)
        writer.write_datetime_value("expectedArrival", self.expected_arrival)
        writer.write_str_value("id", self.id)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineName", self.line_name)
        writer.write_str_value("modeName", self.mode_name)
        writer.write_str_value("naptanId", self.naptan_id)
        writer.write_int_value("operationType", self.operation_type)
        writer.write_str_value("platformName", self.platform_name)
        writer.write_str_value("stationName", self.station_name)
        writer.write_datetime_value("timeToLive", self.time_to_live)
        writer.write_int_value("timeToStation", self.time_to_station)
        writer.write_datetime_value("timestamp", self.timestamp)
        writer.write_object_value("timing", self.timing)
        writer.write_str_value("towards", self.towards)
        writer.write_str_value("vehicleId", self.vehicle_id)
        writer.write_additional_data_value(self.additional_data)
    

