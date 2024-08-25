from pydantic import BaseModel, ConfigDict

__all__ = ["AIChatBaseModel"]


class AIChatBaseModel(BaseModel):
    # Avoid using alias_generator=to_camel to prevent unwanted camel casing of all fields.
    # Set aliases individually for fields that need camel casing. (e.g. session_state)
    model_config = ConfigDict(from_attributes=True, populate_by_name=True)
