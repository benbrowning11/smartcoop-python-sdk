from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any
from .group_subset import GroupSubset

@dataclass(frozen=True)
class User:
    firstName: str
    lastName: str
    userId: Optional[str] = None
    emailAddress: Optional[str] = None
    siteLink: Optional[str] = None
    invites: Optional[list[GroupSubset]] = None

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> User:
        return User(
            userId=json_data.get('userId'),
            firstName=json_data['firstName'],
            lastName=json_data['lastName'],
            emailAddress=json_data.get('emailAddress'),
            siteLink=json_data.get('siteLink'),
            invites=[GroupSubset.from_json(invite) for invite in json_data['invites']] if json_data.get('invites') else None
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "userId": self.userId,
            "firstName": self.firstName,
            "lastName": self.lastName,
            "emailAddress": self.emailAddress,
            "siteLink": self.siteLink,
            "invites": [invite.to_json() for invite in self.invites] if self.invites else None
        }
