from typing import Generic, List, Optional

from .base import AIChatBaseModel
from .file_param_pydantic import AIChatFileParamModel
from .role import AIChatRole
from .type_var import ContextT

__all__ = ["AIChatMessageParamModel"]


class AIChatMessageParamModel(AIChatBaseModel, Generic[ContextT]):
    role: AIChatRole
    content: str
    context: Optional[ContextT] = None
    files: Optional[List[AIChatFileParamModel]] = None
