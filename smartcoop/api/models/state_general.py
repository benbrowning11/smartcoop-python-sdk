from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class StateGeneral:
    firmwareVersionCurrent: str
    firmwareVersionPrevious: str
    firmwareLastCheck: str
    batteryLevel: int
    powerSource: str
    uptime: int
    displayLine1: str
    displayLine2: str   

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> StateGeneral:
        return StateGeneral(
            firmwareVersionCurrent=json_data['firmwareVersionCurrent'],
            firmwareVersionPrevious=json_data['firmwareVersionPrevious'],
            firmwareLastCheck=json_data['firmwareLastCheck'],
            batteryLevel=json_data['batteryLevel'],
            powerSource=json_data['powerSource'],
            uptime=json_data['uptime'],
            displayLine1=json_data.get('displayLine1', ''),
            displayLine2=json_data.get('displayLine2', '')
        )
