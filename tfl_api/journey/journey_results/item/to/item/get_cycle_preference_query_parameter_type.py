from enum import Enum

class GetCyclePreferenceQueryParameterType(str, Enum):
    None_ = "None",
    LeaveAtStation = "LeaveAtStation",
    TakeOnTransport = "TakeOnTransport",
    AllTheWay = "AllTheWay",
    CycleHire = "CycleHire",

