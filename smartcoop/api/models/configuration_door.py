from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ConfigurationDoor:
    doorType: str
    openMode: str
    openDelay: int
    openLightLevel: int
    openTime: str
    closeMode: str
    closeDelay: int
    closeLightLevel: int
    closeTime: str
    colour: str

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> ConfigurationDoor:
        return ConfigurationDoor(
            doorType=json_data['doorType'],
            openMode=json_data['openMode'],
            openDelay=json_data['openDelay'],
            openLightLevel=json_data['openLightLevel'],
            openTime=json_data['openTime'],
            closeMode=json_data['closeMode'],
            closeDelay=json_data['closeDelay'],
            closeLightLevel=json_data['closeLightLevel'],
            closeTime=json_data['closeTime'],
            colour=json_data['colour']
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "doorType": self.doorType,
            "openMode": self.openMode,
            "openDelay": self.openDelay,
            "openLightLevel": self.openLightLevel,
            "openTime": self.openTime,
            "closeMode": self.closeMode,
            "closeDelay": self.closeDelay,
            "closeLightLevel": self.closeLightLevel,
            "closeTime": self.closeTime,
            "colour": self.colour
        }
