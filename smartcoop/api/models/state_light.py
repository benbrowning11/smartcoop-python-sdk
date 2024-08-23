from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class StateLight:
    state: str

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> StateLight:
        return StateLight(
            state=json_data['state']
        )
