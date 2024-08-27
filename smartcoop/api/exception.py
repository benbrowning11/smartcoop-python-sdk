

class SetValueNotFoundError(Exception):
    def __init__(self, setValue: str, deviceName: str | None = None):
        self.deviceName = deviceName
        self.setValue = setValue
        message = f"Set: '{setValue}' not found" 
        if deviceName:
            message += f" for device: '{deviceName}'"
        super().__init__(message)

class ParameterValueNotFoundError(Exception):
    def __init__(self, setValue: str, parameterValue: str, deviceName: str | None = None):
        self.deviceName = deviceName
        self.setValue = setValue
        self.parameterValue = parameterValue
        message = f"Parameter value: '{parameterValue}' not found in set: '{setValue}'"
        if deviceName:
            message += f" for device: '{deviceName}'"
        super().__init__(message)

class KeyFormatError(Exception):
    def __init__(self, key: str):
        self.key = key
        message = f"Invalid key format: " + key + ". Expected format: 'set.value' or tuple['set', 'value']"
        super().__init__(message)