from pydantic import BaseModel
from typing import Optional

# Base model
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    completed: bool = False
