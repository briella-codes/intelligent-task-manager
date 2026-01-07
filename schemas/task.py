from datetime import date
from pydantic import BaseModel, Field
from typing import Optional

#clean for client
class TaskResponse(BaseModel):
    id: int
    title: str = Field(min_length=1, max_length=100)
    description: str | None = Field(max_length = 500)
    priority: int = Field(ge=1,le=3)
    status : str
    due_date: date | None = None

"""
class TaskCreate(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    description: str = Field(max_length = 500)
    priority : int = Field(ge=1,le=3)
    due_date : date

class TaskUpdate(BaseModel):
    title: str | None
    description: str | None
    priority : int | None = Field(ge=1,le=3)
    status: str | None
    due_date: date | None = None
"""