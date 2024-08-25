from .base import AIChatBaseModel

__all__ = ["AIChatError", "AIChatErrorResponse"]


class AIChatError(AIChatBaseModel):
    code: str
    message: str


class AIChatErrorResponse(AIChatBaseModel):
    error: AIChatError
