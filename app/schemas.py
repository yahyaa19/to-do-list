# Pydantic models for request/response validation.

from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str
    priority: int

class TaskCreate(TaskBase):
    pass

class TaskUpdate(TaskBase):
    title: str | None = None
    description: str | None = None
    priority: int | None = None
    completed: bool | None = None

class Task(TaskBase):
    id: int
    completed: bool



