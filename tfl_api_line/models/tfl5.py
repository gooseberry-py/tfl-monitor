from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .tfl3 import Tfl3
    from .tfl4 import Tfl4

@dataclass
class Tfl5(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Busiest times at a station (static information)
    passenger_flows: Optional[list[Tfl3]] = None
    # Train Loading on a scale 1-6, 1 being "Very quiet" and 6 being "Exceptionally busy" (static information)
    train_loadings: Optional[list[Tfl4]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Tfl5:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Tfl5
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Tfl5()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .tfl3 import Tfl3
        from .tfl4 import Tfl4

        from .tfl3 import Tfl3
        from .tfl4 import Tfl4

        fields: dict[str, Callable[[Any], None]] = {
            "passengerFlows": lambda n : setattr(self, 'passenger_flows', n.get_collection_of_object_values(Tfl3)),
            "trainLoadings": lambda n : setattr(self, 'train_loadings', n.get_collection_of_object_values(Tfl4)),
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
        writer.write_collection_of_object_values("passengerFlows", self.passenger_flows)
        writer.write_collection_of_object_values("trainLoadings", self.train_loadings)
        writer.write_additional_data_value(self.additional_data)
    

