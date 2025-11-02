from enum import Enum

class ArrivalDeparture_departureStatus(str, Enum):
    OnTime = "OnTime",
    Delayed = "Delayed",
    Cancelled = "Cancelled",
    NotStoppingAtStation = "NotStoppingAtStation",

