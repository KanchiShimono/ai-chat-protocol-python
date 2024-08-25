from typing import Generic, List, Optional

from typing_extensions import Required, TypedDict

from .message_param import AIChatMessageParam
from .type_var import ContextT, MessageContextT, SessionStateT

__all__ = ["AIChatCompletionRequestParam"]


class AIChatCompletionRequestParam(Generic[ContextT, SessionStateT, MessageContextT], TypedDict, total=False):
    messages: Required[List[AIChatMessageParam[MessageContextT]]]
    context: Optional[ContextT]
    session_state: Optional[SessionStateT]
