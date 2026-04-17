import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    commuter = "commuter"
    conductor = "conductor"
    driver = "driver"
    operator = "operator"
