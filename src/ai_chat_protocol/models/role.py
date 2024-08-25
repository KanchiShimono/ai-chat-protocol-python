from typing import Literal

from typing_extensions import TypeAlias

__all__ = ["AIChatRole"]


AIChatRole: TypeAlias = Literal["user", "assistant", "system"]
