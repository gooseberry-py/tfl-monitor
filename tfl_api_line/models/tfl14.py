from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl11 import Tfl11
    from .tfl13 import Tfl13
    from .tfl14_category import Tfl14_category

@dataclass
class Tfl14(AdditionalDataHolder, Parsable):
    """
    Represents a disruption to a route within the transport network.
    """
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Gets or sets the additionaInfo of this disruption.
    additional_info: Optional[str] = None
    # Gets or sets the routes affected by this disruption
    affected_routes: Optional[list[Tfl13]] = None
    # Gets or sets the stops affected by this disruption
    affected_stops: Optional[list[Tfl11]] = None
    # Gets or sets the category of this dispruption.
    category: Optional[Tfl14_category] = None
    # Gets or sets the description of the category.
    category_description: Optional[str] = None
    # Text describing the closure type
    closure_text: Optional[str] = None
    # Gets or sets the date/time when this disruption was created.
    created: Optional[datetime.datetime] = None
    # Gets or sets the description of this disruption.
    description: Optional[str] = None
    # Gets or sets the date/time when this disruption was last updated.
    last_update: Optional[datetime.datetime] = None
    # Gets or sets the summary of this disruption.
    summary: Optional[str] = None
    # Gets or sets the disruption type of this dispruption.
    type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl14:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl14
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl14()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl11 import Tfl11
        from .tfl13 import Tfl13
        from .tfl14_category import Tfl14_category

        from .tfl11 import Tfl11
        from .tfl13 import Tfl13
        from .tfl14_category import Tfl14_category

        fields: dict[str, Callable[[Any], None]] = {
            "additionalInfo": lambda n : setattr(self, 'additional_info', n.get_str_value()),
            "affectedRoutes": lambda n : setattr(self, 'affected_routes', n.get_collection_of_object_values(Tfl13)),
            "affectedStops": lambda n : setattr(self, 'affected_stops', n.get_collection_of_object_values(Tfl11)),
            "category": lambda n : setattr(self, 'category', n.get_enum_value(Tfl14_category)),
            "categoryDescription": lambda n : setattr(self, 'category_description', n.get_str_value()),
            "closureText": lambda n : setattr(self, 'closure_text', n.get_str_value()),
            "created": lambda n : setattr(self, 'created', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "lastUpdate": lambda n : setattr(self, 'last_update', n.get_datetime_value()),
            "summary": lambda n : setattr(self, 'summary', n.get_str_value()),
            "type": lambda n : setattr(self, 'type', n.get_str_value()),
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
        writer.write_str_value("additionalInfo", self.additional_info)
        writer.write_collection_of_object_values("affectedRoutes", self.affected_routes)
        writer.write_collection_of_object_values("affectedStops", self.affected_stops)
        writer.write_enum_value("category", self.category)
        writer.write_str_value("categoryDescription", self.category_description)
        writer.write_str_value("closureText", self.closure_text)
        writer.write_datetime_value("created", self.created)
        writer.write_str_value("description", self.description)
        writer.write_datetime_value("lastUpdate", self.last_update)
        writer.write_str_value("summary", self.summary)
        writer.write_str_value("type", self.type)
        writer.write_additional_data_value(self.additional_data)
    

