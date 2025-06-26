from pydantic import BaseModel, Field


class Validation(BaseModel):
    valid: bool = Field(
        description="Provides indicator if prompt is following required pattern.",
    )

    recommendation: str | None = Field(
        default=None,
        description="If provided prompt is not following required pattern the recommendation will be provided. "
                    "Recommendation should be short and concise (up to 50 tokens) and describe important moments that "
                    "need to be changed.",
    )