from enum import Enum

class GetWalkingSpeedQueryParameterType(str, Enum):
    Slow = "Slow",
    Average = "Average",
    Fast = "Fast",

