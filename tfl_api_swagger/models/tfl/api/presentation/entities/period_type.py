from enum import Enum

class Period_type(str, Enum):
    Normal = "Normal",
    FrequencyHours = "FrequencyHours",
    FrequencyMinutes = "FrequencyMinutes",
    Unknown = "Unknown",

