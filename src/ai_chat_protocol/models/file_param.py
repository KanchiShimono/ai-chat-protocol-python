from typing_extensions import Required, TypedDict

__all__ = ["AIChatFileParam"]


class AIChatFileParam(TypedDict, total=False):
    content_type: Required[str]
    data: Required[bytes]
