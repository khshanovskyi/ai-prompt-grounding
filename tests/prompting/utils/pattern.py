from enum import StrEnum


class PromptPattern(StrEnum):
    ZERO_SHOT = "Zero-shot"
    ONE_SHOT = "One-shot"
    FEW_SHOT = "Few-Shot"
    CHAIN_OF_THOUGHT = "Chain-of-Thought"
    ROLE_BASED = "Role-Based"
    PERSONA_PATTERN = "Persona Pattern"
    CONSTRAINT_PATTERN = "Constraint Pattern"
    TEMPLATE_PATTERN = "Template Pattern"