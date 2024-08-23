from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class ConfigurationConnectivity:
    wifiState: str

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> ConfigurationConnectivity:
        return ConfigurationConnectivity(
            wifiState=json_data['wifiState']
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "wifiState": self.wifiState
        }
