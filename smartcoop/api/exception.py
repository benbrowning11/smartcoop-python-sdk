from .models.device import Device

class SetValueNotFoundError(Exception):
    def __init__(self, setValue: str, device: Device | None = None):
        self.device = device
        self.setValue = setValue
        message = f"Set: '{setValue}' not found" 
        if device:
            message += f" for device: '{device.deviceId}'"
        super().__init__(message)

class ParameterValueNotFoundError(Exception):
    def __init__(self, setValue: str, parameterValue: str, device: Device | None = None):
        self.device = device
        self.setValue = setValue
        self.parameterValue = parameterValue
        message = f"Parameter value: '{parameterValue}' not found in set: '{setValue}'"
        if device:
            message += f" for device: '{device.deviceId}'"
        super().__init__(message)

class KeyFormatError(Exception):
    def __init__(self, key: str):
        self.key = key
        message = f"Invalid key format: " + key + ". Expected format: 'set.value' or tuple['set', 'value']"
        super().__init__(message)