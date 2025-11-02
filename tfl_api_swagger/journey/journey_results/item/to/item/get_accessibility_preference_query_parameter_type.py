from enum import Enum

class GetAccessibilityPreferenceQueryParameterType(str, Enum):
    NoRequirements = "NoRequirements",
    NoSolidStairs = "NoSolidStairs",
    NoEscalators = "NoEscalators",
    NoElevators = "NoElevators",
    StepFreeToVehicle = "StepFreeToVehicle",
    StepFreeToPlatform = "StepFreeToPlatform",

