from __future__ import annotations
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .instruction_step_sky_direction_description import InstructionStep_skyDirectionDescription
    from .instruction_step_track_type import InstructionStep_trackType
    from .path_attribute import PathAttribute

@dataclass
class InstructionStep(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The atcoCode property
    atco_code: Optional[str] = None
    # The cumulativeDistance property
    cumulative_distance: Optional[int] = None
    # The cumulativeTravelTime property
    cumulative_travel_time: Optional[int] = None
    # The description property
    description: Optional[str] = None
    # The descriptionHeading property
    description_heading: Optional[str] = None
    # The distance property
    distance: Optional[int] = None
    # The latitude property
    latitude: Optional[float] = None
    # The longitude property
    longitude: Optional[float] = None
    # The pathAttribute property
    path_attribute: Optional[PathAttribute] = None
    # The skyDirection property
    sky_direction: Optional[int] = None
    # The skyDirectionDescription property
    sky_direction_description: Optional[InstructionStep_skyDirectionDescription] = None
    # The streetName property
    street_name: Optional[str] = None
    # The trackType property
    track_type: Optional[InstructionStep_trackType] = None
    # The travelTime property
    travel_time: Optional[int] = None
    # The turnDirection property
    turn_direction: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> InstructionStep:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: InstructionStep
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return InstructionStep()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .instruction_step_sky_direction_description import InstructionStep_skyDirectionDescription
        from .instruction_step_track_type import InstructionStep_trackType
        from .path_attribute import PathAttribute

        from .instruction_step_sky_direction_description import InstructionStep_skyDirectionDescription
        from .instruction_step_track_type import InstructionStep_trackType
        from .path_attribute import PathAttribute

        fields: dict[str, Callable[[Any], None]] = {
            "atcoCode": lambda n : setattr(self, 'atco_code', n.get_str_value()),
            "cumulativeDistance": lambda n : setattr(self, 'cumulative_distance', n.get_int_value()),
            "cumulativeTravelTime": lambda n : setattr(self, 'cumulative_travel_time', n.get_int_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "descriptionHeading": lambda n : setattr(self, 'description_heading', n.get_str_value()),
            "distance": lambda n : setattr(self, 'distance', n.get_int_value()),
            "latitude": lambda n : setattr(self, 'latitude', n.get_float_value()),
            "longitude": lambda n : setattr(self, 'longitude', n.get_float_value()),
            "pathAttribute": lambda n : setattr(self, 'path_attribute', n.get_object_value(PathAttribute)),
            "skyDirection": lambda n : setattr(self, 'sky_direction', n.get_int_value()),
            "skyDirectionDescription": lambda n : setattr(self, 'sky_direction_description', n.get_enum_value(InstructionStep_skyDirectionDescription)),
            "streetName": lambda n : setattr(self, 'street_name', n.get_str_value()),
            "trackType": lambda n : setattr(self, 'track_type', n.get_enum_value(InstructionStep_trackType)),
            "travelTime": lambda n : setattr(self, 'travel_time', n.get_int_value()),
            "turnDirection": lambda n : setattr(self, 'turn_direction', n.get_str_value()),
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
        writer.write_str_value("atcoCode", self.atco_code)
        writer.write_int_value("cumulativeDistance", self.cumulative_distance)
        writer.write_int_value("cumulativeTravelTime", self.cumulative_travel_time)
        writer.write_str_value("description", self.description)
        writer.write_str_value("descriptionHeading", self.description_heading)
        writer.write_int_value("distance", self.distance)
        writer.write_float_value("latitude", self.latitude)
        writer.write_float_value("longitude", self.longitude)
        writer.write_object_value("pathAttribute", self.path_attribute)
        writer.write_int_value("skyDirection", self.sky_direction)
        writer.write_enum_value("skyDirectionDescription", self.sky_direction_description)
        writer.write_str_value("streetName", self.street_name)
        writer.write_enum_value("trackType", self.track_type)
        writer.write_int_value("travelTime", self.travel_time)
        writer.write_str_value("turnDirection", self.turn_direction)
        writer.write_additional_data_value(self.additional_data)
    

