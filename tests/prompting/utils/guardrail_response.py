from pydantic import BaseModel, Field

class ManipulationDetection(BaseModel):
    manipulation_detected: bool = Field(
        description="Provides indicator if manipulation detected.",
    )

    recommendation: str | None = Field(
        default=None,
        description="If manipulation is detected, provides recommendation. Recommendation have to short and concise "
                    "(up to 50 tokens)! Here need to indicate that the prompt need to be changed in place where manipulation is detected.",
    )