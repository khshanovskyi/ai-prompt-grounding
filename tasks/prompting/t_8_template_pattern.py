"""
Template Pattern:

A prompt that provides a rigid, predefined structural template with specific sections, labels, and formatting that the
AI must follow exactly without deviation.

Sample formats: Markdown, XML
Sample:
    Analyze the following business scenario using this template:
        SITUATION: [Brief description]
        STAKEHOLDERS: [List key parties involved]
        CHALLENGES: [Identify main problems]
        OPPORTUNITIES: [Potential benefits]
        RECOMMENDATIONS: [Specific actions]
        NEXT STEPS: [Immediate actions needed]

    **Scenario**: `A local restaurant wants to start online delivery`
"""

#TODO:
# 1. Add 3 prompts with template pattern (Markdown, XML)
# 2. Test your solution: run tests.prompting.test_8_template_pattern.TemplatePromptTest#test
# 3. Check test output for validation

PROMPTS = [
    # Markdown-based template
    """Analyze this project using the markdown template:
    
    ## PROJECT
    **Name:** [Project name]
    **Description:** [One sentence]
    
    ## SCOPE
    **Included:** [What's in]
    **Excluded:** [What's out]
    
    ## RISKS
    1. [Risk 1]
    2. [Risk 2]
    
    ## DELIVERABLES
    - [Output 1]
    - [Output 2]
    
    Project: Building a mobile app for food delivery in small towns.""",

    # XML-based template
    """Analyze this problem using the XML template:
    
    <analysis>
        <problem>
            <description>[Main issue]</description>
            <severity>[High/Medium/Low]</severity>
        </problem>
        <solution>
            <recommendation>[Proposed fix]</recommendation>
            <timeline>[Time needed]</timeline>
        </solution>
        <outcome>
            <benefit>[Expected result]</benefit>
            <metric>[How to measure]</metric>
        </outcome>
    </analysis>
    
    Problem: Company's customer support response time is 3 days, customers are complaining.""",

    """
    Analyze the following business scenario using this template:
        SITUATION: [Brief description]
        STAKEHOLDERS: [List key parties involved]
        CHALLENGES: [Identify main problems]
        OPPORTUNITIES: [Potential benefits]
        RECOMMENDATIONS: [Specific actions]
        NEXT STEPS: [Immediate actions needed]
        
    **Scenario**: `A local restaurant wants to start online delivery`
    """
]