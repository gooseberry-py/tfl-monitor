from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .timetable_route import TimetableRoute

@dataclass
class Timetable(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The departureStopId property
    departure_stop_id: Optional[str] = None
    # The routes property
    routes: Optional[list[TimetableRoute]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Timetable:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Timetable
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Timetable()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .timetable_route import TimetableRoute

        from .timetable_route import TimetableRoute

        fields: dict[str, Callable[[Any], None]] = {
            "departureStopId": lambda n : setattr(self, 'departure_stop_id', n.get_str_value()),
            "routes": lambda n : setattr(self, 'routes', n.get_collection_of_object_values(TimetableRoute)),
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
        writer.write_str_value("departureStopId", self.departure_stop_id)
        writer.write_collection_of_object_values("routes", self.routes)
        writer.write_additional_data_value(self.additional_data)
    

