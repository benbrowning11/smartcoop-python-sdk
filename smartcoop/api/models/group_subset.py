from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class GroupSubset:
    groupId: str
    groupName: str
    access: str

    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> GroupSubset:
        return cls(
            groupId=json_data['groupId'],
            groupName=json_data['groupName'],
            access=json_data['access']
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "groupId": self.groupId,
            "groupName": self.groupName,
            "access": self.access
        }
