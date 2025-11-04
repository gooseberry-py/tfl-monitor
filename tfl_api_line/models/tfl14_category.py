from enum import Enum

class Tfl14_category(str, Enum):
    Undefined = "Undefined",
    RealTime = "RealTime",
    PlannedWork = "PlannedWork",
    Information = "Information",
    Event = "Event",
    Crowding = "Crowding",
    StatusAlert = "StatusAlert",

