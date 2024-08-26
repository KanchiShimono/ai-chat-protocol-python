from pydantic import Field

from .base import AIChatBaseModel

__all__ = ["AIChatFileParamModel"]


class AIChatFileParamModel(AIChatBaseModel):
    content_type: str = Field(..., alias="contentType")
    data: bytes
