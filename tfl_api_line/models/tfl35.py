from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl29 import Tfl29
    from .tfl34 import Tfl34

@dataclass
class Tfl35(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The schedules property
    schedules: Optional[list[Tfl34]] = None
    # The stationIntervals property
    station_intervals: Optional[list[Tfl29]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl35:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl35
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl35()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl29 import Tfl29
        from .tfl34 import Tfl34

        from .tfl29 import Tfl29
        from .tfl34 import Tfl34

        fields: dict[str, Callable[[Any], None]] = {
            "schedules": lambda n : setattr(self, 'schedules', n.get_collection_of_object_values(Tfl34)),
            "stationIntervals": lambda n : setattr(self, 'station_intervals', n.get_collection_of_object_values(Tfl29)),
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
        writer.write_collection_of_object_values("schedules", self.schedules)
        writer.write_collection_of_object_values("stationIntervals", self.station_intervals)
        writer.write_additional_data_value(self.additional_data)
    

