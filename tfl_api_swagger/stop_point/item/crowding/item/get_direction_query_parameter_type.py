from enum import Enum

class GetDirectionQueryParameterType(str, Enum):
    Inbound = "inbound",
    Outbound = "outbound",
    All = "all",

