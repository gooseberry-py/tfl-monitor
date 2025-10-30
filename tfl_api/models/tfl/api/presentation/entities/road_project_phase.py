from enum import Enum

class RoadProject_phase(str, Enum):
    Unscoped = "Unscoped",
    Concept = "Concept",
    ConsultationEnded = "ConsultationEnded",
    Consultation = "Consultation",
    Construction = "Construction",
    Complete = "Complete",

