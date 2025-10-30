from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .road_project_phase import RoadProject_phase

@dataclass
class RoadProject(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # The boroughsBenefited property
    boroughs_benefited: Optional[list[str]] = None
    # The constructionEndDate property
    construction_end_date: Optional[datetime.datetime] = None
    # The constructionStartDate property
    construction_start_date: Optional[datetime.datetime] = None
    # The consultationEndDate property
    consultation_end_date: Optional[datetime.datetime] = None
    # The consultationPageUrl property
    consultation_page_url: Optional[str] = None
    # The consultationStartDate property
    consultation_start_date: Optional[datetime.datetime] = None
    # The contactEmail property
    contact_email: Optional[str] = None
    # The contactName property
    contact_name: Optional[str] = None
    # The cycleSuperhighwayId property
    cycle_superhighway_id: Optional[str] = None
    # The externalPageUrl property
    external_page_url: Optional[str] = None
    # The phase property
    phase: Optional[RoadProject_phase] = None
    # The projectDescription property
    project_description: Optional[str] = None
    # The projectId property
    project_id: Optional[str] = None
    # The projectName property
    project_name: Optional[str] = None
    # The projectPageUrl property
    project_page_url: Optional[str] = None
    # The projectSummaryPageUrl property
    project_summary_page_url: Optional[str] = None
    # The schemeName property
    scheme_name: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoadProject:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoadProject
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoadProject()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .road_project_phase import RoadProject_phase

        from .road_project_phase import RoadProject_phase

        fields: dict[str, Callable[[Any], None]] = {
            "boroughsBenefited": lambda n : setattr(self, 'boroughs_benefited', n.get_collection_of_primitive_values(str)),
            "constructionEndDate": lambda n : setattr(self, 'construction_end_date', n.get_datetime_value()),
            "constructionStartDate": lambda n : setattr(self, 'construction_start_date', n.get_datetime_value()),
            "consultationEndDate": lambda n : setattr(self, 'consultation_end_date', n.get_datetime_value()),
            "consultationPageUrl": lambda n : setattr(self, 'consultation_page_url', n.get_str_value()),
            "consultationStartDate": lambda n : setattr(self, 'consultation_start_date', n.get_datetime_value()),
            "contactEmail": lambda n : setattr(self, 'contact_email', n.get_str_value()),
            "contactName": lambda n : setattr(self, 'contact_name', n.get_str_value()),
            "cycleSuperhighwayId": lambda n : setattr(self, 'cycle_superhighway_id', n.get_str_value()),
            "externalPageUrl": lambda n : setattr(self, 'external_page_url', n.get_str_value()),
            "phase": lambda n : setattr(self, 'phase', n.get_enum_value(RoadProject_phase)),
            "projectDescription": lambda n : setattr(self, 'project_description', n.get_str_value()),
            "projectId": lambda n : setattr(self, 'project_id', n.get_str_value()),
            "projectName": lambda n : setattr(self, 'project_name', n.get_str_value()),
            "projectPageUrl": lambda n : setattr(self, 'project_page_url', n.get_str_value()),
            "projectSummaryPageUrl": lambda n : setattr(self, 'project_summary_page_url', n.get_str_value()),
            "schemeName": lambda n : setattr(self, 'scheme_name', n.get_str_value()),
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
        writer.write_collection_of_primitive_values("boroughsBenefited", self.boroughs_benefited)
        writer.write_datetime_value("constructionEndDate", self.construction_end_date)
        writer.write_datetime_value("constructionStartDate", self.construction_start_date)
        writer.write_datetime_value("consultationEndDate", self.consultation_end_date)
        writer.write_str_value("consultationPageUrl", self.consultation_page_url)
        writer.write_datetime_value("consultationStartDate", self.consultation_start_date)
        writer.write_str_value("contactEmail", self.contact_email)
        writer.write_str_value("contactName", self.contact_name)
        writer.write_str_value("cycleSuperhighwayId", self.cycle_superhighway_id)
        writer.write_str_value("externalPageUrl", self.external_page_url)
        writer.write_enum_value("phase", self.phase)
        writer.write_str_value("projectDescription", self.project_description)
        writer.write_str_value("projectId", self.project_id)
        writer.write_str_value("projectName", self.project_name)
        writer.write_str_value("projectPageUrl", self.project_page_url)
        writer.write_str_value("projectSummaryPageUrl", self.project_summary_page_url)
        writer.write_str_value("schemeName", self.scheme_name)
        writer.write_additional_data_value(self.additional_data)
    

