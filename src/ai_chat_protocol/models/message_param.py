from typing import Generic, List, Optional

from typing_extensions import Required, TypedDict

from .file_param import AIChatFileParam
from .role import AIChatRole
from .type_var import ContextT

__all__ = ["AIChatMessageParam"]


class AIChatMessageParam(Generic[ContextT], TypedDict, total=False):
    role: Required[AIChatRole]
    content: Required[str]
    context: Optional[ContextT]
    files: Optional[List[AIChatFileParam]]
