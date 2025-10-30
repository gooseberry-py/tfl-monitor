from enum import Enum

class Identifier_status(str, Enum):
    Unknown = "Unknown",
    All = "All",
    Open = "Open",
    InProgress = "In Progress",
    Planned = "Planned",
    PlannedSubjectToFeasibilityAndConsultation = "Planned - Subject to feasibility and consultation.",
    NotOpen = "Not Open",

