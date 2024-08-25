from typing import Any, Dict

from typing_extensions import TypeVar

__all__ = ["ContextT", "SessionStateT", "MessageContextT"]


ContextT = TypeVar("ContextT", default=Dict[str, Any])
SessionStateT = TypeVar("SessionStateT", default=Any)
MessageContextT = TypeVar("MessageContextT", default=Dict[str, Any])
