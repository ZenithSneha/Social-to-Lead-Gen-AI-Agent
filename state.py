from typing import Optional, List
from pydantic import BaseModel


class AgentState(BaseModel):
    message: Optional[str] = None
    response: Optional[str] = None
    intent: Optional[str] = None
    name: Optional[str] = None
    email: Optional[str] = None
    platform: Optional[str] = None
    conversation_history: List[str] = []
