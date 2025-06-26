from tests.prompting.utils.guardrail_response import ManipulationDetection
from tests.prompting.utils.validation_response import Validation


class TestResult:

    def __init__(self,
                 content: str,
                 manipulation: ManipulationDetection,
                 response: str | None = None,
                 validation: Validation | None = None
                 ):
        self.content: str = content
        self.manipulation: ManipulationDetection = manipulation
        self.response: str | None = response
        self.validation: Validation | None = validation