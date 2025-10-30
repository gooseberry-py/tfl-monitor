from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .passenger_flow import PassengerFlow
    from .train_loading import TrainLoading

@dataclass
class Crowding(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Busiest times at a station (static information)
    passenger_flows: Optional[list[PassengerFlow]] = None
    # Train Loading on a scale 1-6, 1 being "Very quiet" and 6 being "Exceptionally busy" (static information)
    train_loadings: Optional[list[TrainLoading]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> Crowding:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: Crowding
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return Crowding()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .passenger_flow import PassengerFlow
        from .train_loading import TrainLoading

        from .passenger_flow import PassengerFlow
        from .train_loading import TrainLoading

        fields: dict[str, Callable[[Any], None]] = {
            "passengerFlows": lambda n : setattr(self, 'passenger_flows', n.get_collection_of_object_values(PassengerFlow)),
            "trainLoadings": lambda n : setattr(self, 'train_loadings', n.get_collection_of_object_values(TrainLoading)),
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
    

