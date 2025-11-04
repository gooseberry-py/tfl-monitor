from enum import Enum

class Tfl33_type(str, Enum):
    Normal = "Normal",
    FrequencyHours = "FrequencyHours",
    FrequencyMinutes = "FrequencyMinutes",
    Unknown = "Unknown",

