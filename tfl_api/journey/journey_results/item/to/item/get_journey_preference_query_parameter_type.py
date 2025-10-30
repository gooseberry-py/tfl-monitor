from enum import Enum

class GetJourneyPreferenceQueryParameterType(str, Enum):
    LeastInterchange = "LeastInterchange",
    LeastTime = "LeastTime",
    LeastWalking = "LeastWalking",

