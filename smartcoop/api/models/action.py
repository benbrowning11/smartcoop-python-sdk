from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any

@dataclass(frozen=True)
class Action:
    name: str
    description: str
    value: str
    url: str
    pending: Optional[str] = None

    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> Action:
        return Action(
            name=json_data['actionName'],
            description=json_data['description'],
            value=json_data['actionValue'],
            pending=json_data.get('pendingValue'), 
            url=json_data['url']
        )