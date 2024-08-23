from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class StateConnectivity:
    ssid: str
    wifiStrength: str

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> StateConnectivity:
        return StateConnectivity(
            ssid=json_data['ssid'],
            wifiStrength=json_data['wifiStrength']
        )
