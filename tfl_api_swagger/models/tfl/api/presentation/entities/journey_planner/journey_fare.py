from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .fare import Fare
    from .fare_caveat import FareCaveat

@dataclass
class JourneyFare(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The caveats property
    caveats: Optional[list[FareCaveat]] = None
    # The fares property
    fares: Optional[list[Fare]] = None
    # The totalCost property
    total_cost: Optional[int] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> JourneyFare:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: JourneyFare
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return JourneyFare()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .fare import Fare
        from .fare_caveat import FareCaveat

        from .fare import Fare
        from .fare_caveat import FareCaveat

        fields: dict[str, Callable[[Any], None]] = {
            "caveats": lambda n : setattr(self, 'caveats', n.get_collection_of_object_values(FareCaveat)),
            "fares": lambda n : setattr(self, 'fares', n.get_collection_of_object_values(Fare)),
            "totalCost": lambda n : setattr(self, 'total_cost', n.get_int_value()),
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
        writer.write_collection_of_object_values("caveats", self.caveats)
        writer.write_collection_of_object_values("fares", self.fares)
        writer.write_int_value("totalCost", self.total_cost)
        writer.write_additional_data_value(self.additional_data)
    

