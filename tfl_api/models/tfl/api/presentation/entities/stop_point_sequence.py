from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .matched_stop import MatchedStop
    from .stop_point_sequence_service_type import StopPointSequence_serviceType

@dataclass
class StopPointSequence(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The id of this branch.
    branch_id: Optional[int] = None
    # The direction property
    direction: Optional[str] = None
    # The lineId property
    line_id: Optional[str] = None
    # The lineName property
    line_name: Optional[str] = None
    # The ids of the next branch(es) in the sequence. Note that the next and previous branch id can be            identical in the case of a looped route e.g. the Circle line.
    next_branch_ids: Optional[list[int]] = None
    # The ids of the previous branch(es) in the sequence. Note that the next and previous branch id can be            identical in the case of a looped route e.g. the Circle line.
    prev_branch_ids: Optional[list[int]] = None
    # The serviceType property
    service_type: Optional[StopPointSequence_serviceType] = None
    # The stopPoint property
    stop_point: Optional[list[MatchedStop]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> StopPointSequence:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: StopPointSequence
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return StopPointSequence()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .matched_stop import MatchedStop
        from .stop_point_sequence_service_type import StopPointSequence_serviceType

        from .matched_stop import MatchedStop
        from .stop_point_sequence_service_type import StopPointSequence_serviceType

        fields: dict[str, Callable[[Any], None]] = {
            "branchId": lambda n : setattr(self, 'branch_id', n.get_int_value()),
            "direction": lambda n : setattr(self, 'direction', n.get_str_value()),
            "lineId": lambda n : setattr(self, 'line_id', n.get_str_value()),
            "lineName": lambda n : setattr(self, 'line_name', n.get_str_value()),
            "nextBranchIds": lambda n : setattr(self, 'next_branch_ids', n.get_collection_of_primitive_values(int)),
            "prevBranchIds": lambda n : setattr(self, 'prev_branch_ids', n.get_collection_of_primitive_values(int)),
            "serviceType": lambda n : setattr(self, 'service_type', n.get_enum_value(StopPointSequence_serviceType)),
            "stopPoint": lambda n : setattr(self, 'stop_point', n.get_collection_of_object_values(MatchedStop)),
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
        writer.write_int_value("branchId", self.branch_id)
        writer.write_str_value("direction", self.direction)
        writer.write_str_value("lineId", self.line_id)
        writer.write_str_value("lineName", self.line_name)
        writer.write_collection_of_primitive_values("nextBranchIds", self.next_branch_ids)
        writer.write_collection_of_primitive_values("prevBranchIds", self.prev_branch_ids)
        writer.write_enum_value("serviceType", self.service_type)
        writer.write_collection_of_object_values("stopPoint", self.stop_point)
        writer.write_additional_data_value(self.additional_data)
    

