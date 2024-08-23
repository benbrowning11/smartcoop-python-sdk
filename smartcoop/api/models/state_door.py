from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class StateDoor:
    state: str
    lastOpenTime: str
    lastCloseTime: str
    fault: str
    lightLevel: int
    displayLine1: str
    displayLine2: str       

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> StateDoor:
        return StateDoor(
            state=json_data['state'],
            lastOpenTime=json_data['lastOpenTime'],
            lastCloseTime=json_data['lastCloseTime'],
            fault=json_data['fault'],
            lightLevel=json_data['lightLevel'],
            displayLine1=json_data['displayLine1'],
            displayLine2=json_data['displayLine2']
        )
