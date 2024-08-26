from typing import Generic, List, Optional

from pydantic import Field

from .base import AIChatBaseModel
from .message_param_model import AIChatMessageParamModel
from .type_var import ContextT, MessageContextT, SessionStateT

__all__ = ["AIChatCompletionRequestParamModel"]


class AIChatCompletionRequestParamModel(AIChatBaseModel, Generic[ContextT, SessionStateT, MessageContextT]):
    messages: List[AIChatMessageParamModel[MessageContextT]]
    context: Optional[ContextT] = None
    session_state: Optional[SessionStateT] = Field(None, alias="sessionState")
