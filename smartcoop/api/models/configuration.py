from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from ..exception import SetValueNotFoundError, ParameterValueNotFoundError, KeyFormatError
@dataclass
class Configuration:
    _data: dict[str, dict[str, Any] | None]
        
    def getConfigurationValue(self, key: str | tuple[str, str]) -> dict[str, Any] | None:
        if isinstance(key, str):
            key = key.split('.')
            if len(key) != 2:
                raise KeyFormatError(key)
            
        return self._getFromData(key[0], key[1])
    
    def setConfigurationValue(self, key: str | tuple[str, str], value: Any) -> True:
        if isinstance(key, str):
            key = key.split('.') 
            
        if len(key) != 2 or key[0] is None or key[1] is None:
            raise KeyFormatError(key)
        
        if not self.isSet(key[0]):
            self._data[key[0]] = {}

        self._data[key[0]][key[1]] = value
            
        return True

    def _getFromData(self, setName: str, valueName: str) -> Any:
        if self._data.get(setName) is None or not isinstance(self._data.get(setName), dict):
            raise SetValueNotFoundError(setName)
        elif self._data[setName].get(valueName) is None:
            raise ParameterValueNotFoundError(setName, valueName)
        return self._data[setName][valueName]

    def isSet(self, key: str | tuple[str, str]) -> bool:
        if isinstance(key, str):
            key = key.split('.')
            if len(key) > 2:
                raise KeyFormatError(key)
        return self._data.get(key[0]) is not None \
                and (len(key) == 1 \
                    or self._data[key[0]].get(key[1]) is not None)

    def getAvailableSets(self) -> list[str]:
        return list(self._data.keys())
    
    def getAvailableValues(self, setName: str) -> list[str] | None:
        if not self.isSet(setName):
            return None
        return list(self._data[setName].keys())

    def to_json(self) -> dict[str, dict[str, Any] | None]:
        return self._data

    @classmethod
    def from_json(cls, json_data: dict[str, dict[str, Any] | None]) -> Configuration:
        return cls(_data=json_data)