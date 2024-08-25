from typing import Generic, Optional

from pydantic import Field

from .base import AIChatBaseModel
from .message import AIChatMessage, AIChatMessageDelta
from .type_var import ContextT, MessageContextT, SessionStateT

__all__ = ["AIChatCompletion", "AIChatCompletionDelta"]


class AIChatCompletion(AIChatBaseModel, Generic[ContextT, SessionStateT, MessageContextT]):
    message: AIChatMessage[MessageContextT]
    context: Optional[ContextT] = None
    session_state: Optional[SessionStateT] = Field(None, alias="sessionState")


class AIChatCompletionDelta(AIChatBaseModel, Generic[ContextT, SessionStateT, MessageContextT]):
    delta: AIChatMessageDelta[MessageContextT]
    context: Optional[ContextT] = None
    session_state: Optional[SessionStateT] = Field(None, alias="sessionState")
