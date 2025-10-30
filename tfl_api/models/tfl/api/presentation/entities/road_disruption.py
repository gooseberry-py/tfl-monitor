from __future__ import annotations
import datetime
from collections.abc import Callable
from dataclasses import dataclass, field
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from .....system.data.spatial.db_geography import DbGeography
    from .road_disruption_impact_area import RoadDisruptionImpactArea
    from .road_disruption_line import RoadDisruptionLine
    from .road_disruption_schedule import RoadDisruptionSchedule
    from .road_project import RoadProject
    from .street import Street

@dataclass
class RoadDisruption(AdditionalDataHolder, Parsable):
    # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
    additional_data: dict[str, Any] = field(default_factory=dict)

    # Describes the nature of disruption e.g. Traffic Incidents, Works
    category: Optional[str] = None
    # Full text of comments describing the disruption, including details of any road closures and diversions, where appropriate.
    comments: Optional[str] = None
    # The Ids of affected corridors, if any.
    corridor_ids: Optional[list[str]] = None
    # Text of the most recent update from the LSTCC on the state of the             disruption, including the current traffic impact and any advice to             road users.
    current_update: Optional[str] = None
    # The time when the last CurrentUpdate description was recorded,             or null if no CurrentUpdate has been applied.
    current_update_date_time: Optional[datetime.datetime] = None
    # The date and time on which the disruption ended. For planned disruptions, this date will have a valid value. For unplanned             disruptions in progress, this field will be omitted.
    end_date_time: Optional[datetime.datetime] = None
    # The geography property
    geography: Optional[DbGeography] = None
    # The geometry property
    geometry: Optional[DbGeography] = None
    # True if any of the affected Streets have a "Full Closure" status, false otherwise. A RoadDisruption that has HasClosures is considered a             Severe or Serious disruption for severity filtering purposes.
    has_closures: Optional[bool] = None
    # Unique identifier for the road disruption
    id: Optional[str] = None
    # True if the disruption is planned on a future date that is open to change
    is_provisional: Optional[bool] = None
    # The date and time on which the disruption was last modified in the system. This information can reliably be used by a developer to quickly            compare two instances of the same disruption to determine if it has been changed.
    last_modified_time: Optional[datetime.datetime] = None
    # This describes the level of potential impact on traffic operations of the disruption.             High = e.g. a one-off disruption on a major or high profile route which will require a high level of operational attention             Medium = This is the default value             Low = e.g. a frequently occurring disruption which is well known
    level_of_interest: Optional[str] = None
    # The text of any associated link
    link_text: Optional[str] = None
    # The url of any associated link
    link_url: Optional[str] = None
    # Main road name / number (borough) or preset area name where the disruption is located. This might be useful for a map popup where space is limited.
    location: Optional[str] = None
    # An ordinal of the disruption based on severity, level of interest and corridor.
    ordinal: Optional[int] = None
    # Latitude and longitude (WGS84) of the centroid of the disruption, stored in a geoJSON-formatted string.
    point: Optional[str] = None
    # The publishEndDate property
    publish_end_date: Optional[datetime.datetime] = None
    # TDM Additional properties
    publish_start_date: Optional[datetime.datetime] = None
    # The recurringSchedules property
    recurring_schedules: Optional[list[RoadDisruptionSchedule]] = None
    # The roadDisruptionImpactAreas property
    road_disruption_impact_areas: Optional[list[RoadDisruptionImpactArea]] = None
    # The roadDisruptionLines property
    road_disruption_lines: Optional[list[RoadDisruptionLine]] = None
    # The roadProject property
    road_project: Optional[RoadProject] = None
    # A description of the severity of the disruption.
    severity: Optional[str] = None
    # The date and time which the disruption started. For a planned disruption (i.e. planned road works) this date will be in the future.            For unplanned disruptions, this will default to the date on which the disruption was first recorded, but may be adjusted by the operator.
    start_date_time: Optional[datetime.datetime] = None
    # This describes the status of the disruption.              Active = currently in progress             Active Long Term = currently in progress and long term            Scheduled = scheduled to start within the next 180 days            Recurring Works = planned maintenance works that follow a regular routine or pattern and whose next occurrence is to start within the next 180 days.            Recently Cleared = recently cleared in the last 24 hours            Note that the status of Scheduled or Recurring Works disruptions will change to Active when they start, and will change status again when they end.
    status: Optional[str] = None
    # A collection of zero or more streets affected by the disruption.
    streets: Optional[list[Street]] = None
    # Describes the sub-category of disruption e.g. Collapsed Manhole, Abnormal Load
    sub_category: Optional[str] = None
    # The timeFrame property
    time_frame: Optional[str] = None
    # URL to retrieve this road disruption
    url: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: ParseNode) -> RoadDisruption:
        """
        Creates a new instance of the appropriate class based on discriminator value
        param parse_node: The parse node to use to read the discriminator value and create the object
        Returns: RoadDisruption
        """
        if parse_node is None:
            raise TypeError("parse_node cannot be null.")
        return RoadDisruption()
    
    def get_field_deserializers(self,) -> dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: dict[str, Callable[[ParseNode], None]]
        """
        from .....system.data.spatial.db_geography import DbGeography
        from .road_disruption_impact_area import RoadDisruptionImpactArea
        from .road_disruption_line import RoadDisruptionLine
        from .road_disruption_schedule import RoadDisruptionSchedule
        from .road_project import RoadProject
        from .street import Street

        from .....system.data.spatial.db_geography import DbGeography
        from .road_disruption_impact_area import RoadDisruptionImpactArea
        from .road_disruption_line import RoadDisruptionLine
        from .road_disruption_schedule import RoadDisruptionSchedule
        from .road_project import RoadProject
        from .street import Street

        fields: dict[str, Callable[[Any], None]] = {
            "category": lambda n : setattr(self, 'category', n.get_str_value()),
            "comments": lambda n : setattr(self, 'comments', n.get_str_value()),
            "corridorIds": lambda n : setattr(self, 'corridor_ids', n.get_collection_of_primitive_values(str)),
            "currentUpdate": lambda n : setattr(self, 'current_update', n.get_str_value()),
            "currentUpdateDateTime": lambda n : setattr(self, 'current_update_date_time', n.get_datetime_value()),
            "endDateTime": lambda n : setattr(self, 'end_date_time', n.get_datetime_value()),
            "geography": lambda n : setattr(self, 'geography', n.get_object_value(DbGeography)),
            "geometry": lambda n : setattr(self, 'geometry', n.get_object_value(DbGeography)),
            "hasClosures": lambda n : setattr(self, 'has_closures', n.get_bool_value()),
            "id": lambda n : setattr(self, 'id', n.get_str_value()),
            "isProvisional": lambda n : setattr(self, 'is_provisional', n.get_bool_value()),
            "lastModifiedTime": lambda n : setattr(self, 'last_modified_time', n.get_datetime_value()),
            "levelOfInterest": lambda n : setattr(self, 'level_of_interest', n.get_str_value()),
            "linkText": lambda n : setattr(self, 'link_text', n.get_str_value()),
            "linkUrl": lambda n : setattr(self, 'link_url', n.get_str_value()),
            "location": lambda n : setattr(self, 'location', n.get_str_value()),
            "ordinal": lambda n : setattr(self, 'ordinal', n.get_int_value()),
            "point": lambda n : setattr(self, 'point', n.get_str_value()),
            "publishEndDate": lambda n : setattr(self, 'publish_end_date', n.get_datetime_value()),
            "publishStartDate": lambda n : setattr(self, 'publish_start_date', n.get_datetime_value()),
            "recurringSchedules": lambda n : setattr(self, 'recurring_schedules', n.get_collection_of_object_values(RoadDisruptionSchedule)),
            "roadDisruptionImpactAreas": lambda n : setattr(self, 'road_disruption_impact_areas', n.get_collection_of_object_values(RoadDisruptionImpactArea)),
            "roadDisruptionLines": lambda n : setattr(self, 'road_disruption_lines', n.get_collection_of_object_values(RoadDisruptionLine)),
            "roadProject": lambda n : setattr(self, 'road_project', n.get_object_value(RoadProject)),
            "severity": lambda n : setattr(self, 'severity', n.get_str_value()),
            "startDateTime": lambda n : setattr(self, 'start_date_time', n.get_datetime_value()),
            "status": lambda n : setattr(self, 'status', n.get_str_value()),
            "streets": lambda n : setattr(self, 'streets', n.get_collection_of_object_values(Street)),
            "subCategory": lambda n : setattr(self, 'sub_category', n.get_str_value()),
            "timeFrame": lambda n : setattr(self, 'time_frame', n.get_str_value()),
            "url": lambda n : setattr(self, 'url', n.get_str_value()),
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
        writer.write_str_value("category", self.category)
        writer.write_str_value("comments", self.comments)
        writer.write_collection_of_primitive_values("corridorIds", self.corridor_ids)
        writer.write_str_value("currentUpdate", self.current_update)
        writer.write_datetime_value("currentUpdateDateTime", self.current_update_date_time)
        writer.write_datetime_value("endDateTime", self.end_date_time)
        writer.write_object_value("geography", self.geography)
        writer.write_object_value("geometry", self.geometry)
        writer.write_bool_value("hasClosures", self.has_closures)
        writer.write_str_value("id", self.id)
        writer.write_bool_value("isProvisional", self.is_provisional)
        writer.write_datetime_value("lastModifiedTime", self.last_modified_time)
        writer.write_str_value("levelOfInterest", self.level_of_interest)
        writer.write_str_value("linkText", self.link_text)
        writer.write_str_value("linkUrl", self.link_url)
        writer.write_str_value("location", self.location)
        writer.write_int_value("ordinal", self.ordinal)
        writer.write_str_value("point", self.point)
        writer.write_datetime_value("publishEndDate", self.publish_end_date)
        writer.write_datetime_value("publishStartDate", self.publish_start_date)
        writer.write_collection_of_object_values("recurringSchedules", self.recurring_schedules)
        writer.write_collection_of_object_values("roadDisruptionImpactAreas", self.road_disruption_impact_areas)
        writer.write_collection_of_object_values("roadDisruptionLines", self.road_disruption_lines)
        writer.write_object_value("roadProject", self.road_project)
        writer.write_str_value("severity", self.severity)
        writer.write_datetime_value("startDateTime", self.start_date_time)
        writer.write_str_value("status", self.status)
        writer.write_collection_of_object_values("streets", self.streets)
        writer.write_str_value("subCategory", self.sub_category)
        writer.write_str_value("timeFrame", self.time_frame)
        writer.write_str_value("url", self.url)
        writer.write_additional_data_value(self.additional_data)
    

