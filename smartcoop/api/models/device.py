from __future__ import annotations

from dataclasses import dataclass
from typing import List, Any
from .action import Action
from .configuration import Configuration
from .state import State

@dataclass(frozen=True)
class Device:
    deviceId: str
    name: str
    deviceType: str
    state: State
    configuration: Configuration
    actions: List[Action]

    @classmethod
    def from_json(cls, json_data: dict[str, Any]) -> Device:
        return cls(
            deviceId=json_data['deviceId'],
            name=json_data['name'],
            deviceType=json_data['deviceType'],
            state=State.from_json(json_data['state']),
            configuration=Configuration.from_json(json_data['configuration']),
            actions=[Action.from_json(action) for action in json_data['actions']]
        )

    def tryGetAction(self, action_name: str) -> Action:
        for action in self.actions:
            if action.name == action_name:
                return action
        return None