from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .known_journey import KnownJourney
    from .period import Period

@dataclass
class Schedule(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The firstJourney property
    first_journey: Optional[KnownJourney] = None
    # The knownJourneys property
    known_journeys: Optional[list[KnownJourney]] = None
    # The lastJourney property
    last_journey: Optional[KnownJourney] = None
    # The name property
    name: Optional[str] = None
    # The periods property
    periods: Optional[list[Period]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Schedule:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Schedule
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Schedule()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .known_journey import KnownJourney
        from .period import Period

        from .known_journey import KnownJourney
        from .period import Period

        fields: dict[str, Callable[[Any], None]] = {
            "firstJourney": lambda n : setattr(self, 'first_journey', n.get_object_value(KnownJourney)),
            "knownJourneys": lambda n : setattr(self, 'known_journeys', n.get_collection_of_object_values(KnownJourney)),
            "lastJourney": lambda n : setattr(self, 'last_journey', n.get_object_value(KnownJourney)),
            "name": lambda n : setattr(self, 'name', n.get_str_value()),
            "periods": lambda n : setattr(self, 'periods', n.get_collection_of_object_values(Period)),
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
    

