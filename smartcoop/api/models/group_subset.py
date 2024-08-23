from __future__ import annotations

from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class GroupSubset:
    groupId: str
    groupName: str
    access: str

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> GroupSubset:
        return GroupSubset(
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
