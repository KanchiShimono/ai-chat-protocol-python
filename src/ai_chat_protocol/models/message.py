from typing import Generic, Optional

from .base import AIChatBaseModel
from .role import AIChatRole
from .type_var import ContextT

__all__ = ["AIChatMessage", "AIChatMessageDelta"]


class AIChatMessage(AIChatBaseModel, Generic[ContextT]):
    role: AIChatRole
    content: str
    context: Optional[ContextT] = None


class AIChatMessageDelta(AIChatBaseModel, Generic[ContextT]):
    role: Optional[AIChatRole] = None
    content: Optional[str] = None
    context: Optional[ContextT] = None
