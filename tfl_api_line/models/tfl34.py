from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl30 import Tfl30
    from .tfl33 import Tfl33

@dataclass
class Tfl34(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The firstJourney property
    first_journey: Optional[Tfl30] = None
    # The knownJourneys property
    known_journeys: Optional[list[Tfl30]] = None
    # The lastJourney property
    last_journey: Optional[Tfl30] = None
    # The name property
    name: Optional[str] = None
    # The periods property
    periods: Optional[list[Tfl33]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl34:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl34
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl34()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl30 import Tfl30
        from .tfl33 import Tfl33

        from .tfl30 import Tfl30
        from .tfl33 import Tfl33

        fields: dict[str, Callable[[Any], None]] = {
            "firstJourney": lambda n : setattr(self, 'first_journey', n.get_object_value(Tfl30)),
            "knownJourneys": lambda n : setattr(self, 'known_journeys', n.get_collection_of_object_values(Tfl30)),
            "lastJourney": lambda n : setattr(self, 'last_journey', n.get_object_value(Tfl30)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "periods": lambda n : setattr(self, 'periods', n.get_collection_of_object_values(Tfl33)),
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
        writer.write_object_value("firstJourney", self.first_journey)
        writer.write_collection_of_object_values("knownJourneys", self.known_journeys)
        writer.write_object_value("lastJourney", self.last_journey)
        writer.write_str_value("name", self.name)
        writer.write_collection_of_object_values("periods", self.periods)
        writer.write_additional_data_value(self.additional_data)
    

