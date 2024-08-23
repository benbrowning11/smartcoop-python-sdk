from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ConfigurationLight:
    mode: str
    minutesBeforeClose: int
    maxOnTime: int
    equipped: int

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> ConfigurationLight:
        return ConfigurationLight(
            mode=json_data['mode'],
            minutesBeforeClose=json_data['minutesBeforeClose'],
            maxOnTime=json_data['maxOnTime'],
            equipped=json_data['equipped']
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "mode": self.mode,
            "minutesBeforeClose": self.minutesBeforeClose,
            "maxOnTime": self.maxOnTime,
            "equipped": self.equipped
        }
