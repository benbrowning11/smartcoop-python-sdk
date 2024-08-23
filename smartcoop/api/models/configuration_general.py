from __future__ import annotations

from dataclasses import dataclass
from typing import Optional, Any

@dataclass(frozen=True)
class ConfigurationGeneral:
    datetime: str
    timezone: str
    updateFrequency: int
    language: str
    overnightSleepEnable: bool
    overnightSleepStart: str
    overnightSleepEnd: str
    pollFreq: int
    stayAliveTime: int
    statusUpdatePeriod: int
    useDst: Optional[bool] = None

    @staticmethod
    def from_json(json_data: dict[str, Any]) -> ConfigurationGeneral:
        return ConfigurationGeneral(
            datetime=json_data['datetime'],
            timezone=json_data['timezone'],
            useDst=json_data.get('useDst'),
            updateFrequency=json_data['updateFrequency'],
            language=json_data['language'],
            overnightSleepEnable=json_data['overnightSleepEnable'],
            overnightSleepStart=json_data['overnightSleepStart'],
            overnightSleepEnd=json_data['overnightSleepEnd'],
            pollFreq=json_data['pollFreq'],
            stayAliveTime=json_data['stayAliveTime'],
            statusUpdatePeriod=json_data['statusUpdatePeriod']
        )

    def to_json(self) -> dict[str, Any]:
        return {
            "datetime": self.datetime,
            "timezone": self.timezone,
            "useDst": self.useDst,
            "updateFrequency": self.updateFrequency,
            "language": self.language,
            "overnightSleepEnable": self.overnightSleepEnable,
            "overnightSleepStart": self.overnightSleepStart,
            "overnightSleepEnd": self.overnightSleepEnd,
            "pollFreq": self.pollFreq,
            "stayAliveTime": self.stayAliveTime,
            "statusUpdatePeriod": self.statusUpdatePeriod
        }
