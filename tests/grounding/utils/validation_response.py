from pydantic import BaseModel, Field


class Validation(BaseModel):
    valid: bool = Field(
        description="Provides indicator if grounding has been performed.",
    )

    recommendation: str | None = Field(
        default=None,
        description="If the grounding has not been performed, provide the recommendation of how to to it.",
    )