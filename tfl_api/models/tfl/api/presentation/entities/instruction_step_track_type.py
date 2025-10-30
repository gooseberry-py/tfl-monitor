from enum import Enum

class InstructionStep_trackType(str, Enum):
    Cycleways = "Cycleways",
    CycleSuperHighway = "CycleSuperHighway",
    CanalTowpath = "CanalTowpath",
    QuietRoad = "QuietRoad",
    ProvisionForCyclists = "ProvisionForCyclists",
    BusyRoads = "BusyRoads",
    None_ = "None",
    PushBike = "PushBike",
    Quietway = "Quietway",
    ShuttleBus = "ShuttleBus",
    Ferry = "Ferry",
    CableCar = "CableCar",

