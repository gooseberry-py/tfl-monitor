from enum import Enum

class Identifier_routeType(str, Enum):
    Unknown = "Unknown",
    All = "All",
    CycleSuperhighways = "Cycle Superhighways",
    Quietways = "Quietways",
    Cycleways = "Cycleways",
    MiniHollands = "Mini-Hollands",
    CentralLondonGrid = "Central London Grid",
    StreetspaceRoute = "Streetspace Route",

