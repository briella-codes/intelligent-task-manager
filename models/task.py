from datetime import datetime, date, UTC
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    PENDING = "Pending"
    DONE = "Done"
    PAUSED = "Paused"
    IN_PROGRESS = "in Progress"
    CANCELED = "Canceled"

ALLOWED_ACTIONS = {
    TaskStatus.PENDING : ["done","start","cancel"],
    TaskStatus.DONE : [],
    TaskStatus.PAUSED : ["resume","done","cancel"],
    TaskStatus.IN_PROGRESS : ["done","pause"],
    TaskStatus.CANCELED : ["undo"]
}

class Task:
    id_counter = 0
    def __init__(self, title:str, priority:int, description: str | None = None, status:TaskStatus = TaskStatus.PENDING, due_date: date | None =None, id: int | None = None):
        if id is not None:
            self.id = id
        else:
            self.id = Task.id_counter
            Task.id_counter+=1

        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
        self.due_date = due_date
        self.created_date = datetime.now(UTC)
        self.updated_date = self.created_date
        self.completed_date = None
        self.reschedule_count = 0

        self.next : Optional["Task"]=None
    
    def __str__(self):
        ret = str(self.id) + ", "  + str(self.title) + ", " + str(self.priority)
        return ret
    
    #for the json structure
    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "title": self.title,
            "priority": self.priority,
            "status" : self.status.value,
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
        }
    
    @property
    def status_enum(self) -> TaskStatus:
        return TaskStatus(self.status)