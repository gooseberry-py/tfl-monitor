from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl20 import Tfl20
    from .tfl36 import Tfl36
    from .tfl38 import Tfl38

@dataclass
class Tfl39(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The direction property
    direction: Optional[str] = None
    # The disambiguation property
    disambiguation: Optional[Tfl38] = None
    # The lineId property
    line_id: Optional[str] = None
    # The lineName property
    line_name: Optional[str] = None
    # The pdfUrl property
    pdf_url: Optional[str] = None
    # The stations property
    stations: Optional[list[Tfl20]] = None
    # The statusErrorMessage property
    status_error_message: Optional[str] = None
    # The stops property
    stops: Optional[list[Tfl20]] = None
    # The timetable property
    timetable: Optional[Tfl36] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl39:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl39
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl39()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl20 import Tfl20
        from .tfl36 import Tfl36
        from .tfl38 import Tfl38

        from .tfl20 import Tfl20
        from .tfl36 import Tfl36
        from .tfl38 import Tfl38

        fields: dict[str, Callable[[Any], None]] = {
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "disambiguation": lambda n : setattr(self, 'disambiguation', n.get_object_value(Tfl38)),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineName": lambda n : setattr(self, 'line_name', n.get_str_value()),
            "pdfUrl": lambda n : setattr(self, 'pdf_url', n.get_str_value()),
            "stations": lambda n : setattr(self, 'stations', n.get_collection_of_object_values(Tfl20)),
            "statusErrorMessage": lambda n : setattr(self, 'status_error_message', n.get_str_value()),
            "stops": lambda n : setattr(self, 'stops', n.get_collection_of_object_values(Tfl20)),
            "timetable": lambda n : setattr(self, 'timetable', n.get_object_value(Tfl36)),
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
        writer.write_str_value("direction", self.direction)
        writer.write_object_value("disambiguation", self.disambiguation)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineName", self.line_name)
        writer.write_str_value("pdfUrl", self.pdf_url)
        writer.write_collection_of_object_values("stations", self.stations)
        writer.write_str_value("statusErrorMessage", self.status_error_message)
        writer.write_collection_of_object_values("stops", self.stops)
        writer.write_object_value("timetable", self.timetable)
        writer.write_additional_data_value(self.additional_data)
    

