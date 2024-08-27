from __future__ import annotations

from dataclasses import dataclass
from typing import Any
from ..exception import SetValueNotFoundError, ParameterValueNotFoundError, KeyFormatError

@dataclass(frozen=True)
class State:
    data: dict[str, dict[str, Any] | None]
        
    def getStatusValue(self, key: str | tuple[str, str]) -> dict[str, Any] | None:
        if isinstance(key, str):
            key = key.split('.')
            if len(key) != 2:
                raise KeyFormatError(key)
            
        return self._getFromData(key[0], key[1])

    def _getFromData(self, setName: str, valueName: str) -> Any:
        if self.data.get(setName) is None or not isinstance(self.data.get(setName), dict):
            raise SetValueNotFoundError(setName)
        elif self.data[setName].get(valueName) is None:
            raise ParameterValueNotFoundError(setName, valueName)
        return self.data[setName][valueName]

    def isSet(self, key: str | tuple[str, str]) -> bool:
        if isinstance(key, str):
            key = key.split('.')
            if len(key) > 2:
                raise KeyFormatError(key)
        return self.data.get(key[0]) is not None \
                and (len(key) == 1 \
                    or self.data[key[0]].get(key[1]) is not None)
    
    def getAvailableSets(self) -> list[str]:
        return list(self._data.keys())
    
    def getAvailableValues(self, setName: str) -> list[str] | None:
        if not self.isSet(setName):
            return None
        return list(self._data[setName].keys())
    
    def to_json(self) -> dict[str, dict[str, Any] | None]:
        return self._data

    @classmethod
    def from_json(cls, json_data: dict[str, dict[str, Any] | None]) -> State:
        return cls(_data=json_data)
