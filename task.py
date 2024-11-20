from dataclasses import dataclass
from datetime import datetime

@dataclass
class Task:

    priority: int
    name: str
    description: str
    timestamp: datetime

    def __lt__(self, other):
        return self.priority < other.priority

