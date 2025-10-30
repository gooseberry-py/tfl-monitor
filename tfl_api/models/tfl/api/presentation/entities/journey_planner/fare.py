from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fare_tap import FareTap

@dataclass
class Fare(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The chargeLevel property
    charge_level: Optional[str] = None
    # The chargeProfileName property
    charge_profile_name: Optional[str] = None
    # The cost property
    cost: Optional[int] = None
    # The highZone property
    high_zone: Optional[int] = None
    # The isHopperFare property
    is_hopper_fare: Optional[bool] = None
    # The lowZone property
    low_zone: Optional[int] = None
    # The offPeak property
    off_peak: Optional[int] = None
    # The peak property
    peak: Optional[int] = None
    # The taps property
    taps: Optional[list[FareTap]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Fare:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Fare
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Fare()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fare_tap import FareTap

        from .fare_tap import FareTap

        fields: dict[str, Callable[[Any], None]] = {
            "chargeLevel": lambda n : setattr(self, 'charge_level', n.get_str_value()),
            "chargeProfileName": lambda n : setattr(self, 'charge_profile_name', n.get_str_value()),
            "cost": lambda n : setattr(self, 'cost', n.get_int_value()),
            "highZone": lambda n : setattr(self, 'high_zone', n.get_int_value()),
            "isHopperFare": lambda n : setattr(self, 'is_hopper_fare', n.get_bool_value()),
            "lowZone": lambda n : setattr(self, 'low_zone', n.get_int_value()),
            "offPeak": lambda n : setattr(self, 'off_peak', n.get_int_value()),
            "peak": lambda n : setattr(self, 'peak', n.get_int_value()),
            "taps": lambda n : setattr(self, 'taps', n.get_collection_of_object_values(FareTap)),
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
        writer.write_str_value("chargeLevel", self.charge_level)
        writer.write_str_value("chargeProfileName", self.charge_profile_name)
        writer.write_int_value("cost", self.cost)
        writer.write_int_value("highZone", self.high_zone)
        writer.write_bool_value("isHopperFare", self.is_hopper_fare)
        writer.write_int_value("lowZone", self.low_zone)
        writer.write_int_value("offPeak", self.off_peak)
        writer.write_int_value("peak", self.peak)
        writer.write_collection_of_object_values("taps", self.taps)
        writer.write_additional_data_value(self.additional_data)
    

