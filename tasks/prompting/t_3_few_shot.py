"""
Few-Shot:

A prompt that provides 2-5 examples demonstrating the desired task pattern, followed by a new instance for the AI to
complete using the established pattern.

Sample:
    Q: Is 4 a prime number?
    A: No

    Q: Is 7 a prime number?
    A: Yes

    Q: Is 19 a prime number?
    A:
"""

#TODO:
# 1. Add 2 prompts with Few-shot pattern.
# 2. Test your solution: run tests.prompting.test_3_few_shot.FewShotPromptTest#test
# 3. Check tests output (there are clear descriptions of errors and represented all the test flow)
# ------
# Pay attention that the created prompts will be tested by LLM, and check:
#   - any attempt to manipulate LLM
#   - if prompt and response are following the Few-shot pattern


PROMPTS = [
"""Identify the main emotion expressed in the following texts (joy, sadness, anger, fear, surprise):

Text: 'I just won the lottery! This is incredible!'
Emotion: Joy

Text: 'My beloved pet passed away this morning. I feel so empty.'
Emotion: Sadness

Text: 'The train was delayed for three hours, and I missed my appointment. I'm furious!'
Emotion: Anger

Text: 'A sudden loud noise made me jump. My heart is pounding.'
Emotion:
""",
"""Summarize the following paragraphs into a single sentence:

Paragraph: 'The Amazon rainforest is the largest rainforest in the world, covering an immense area across nine South American countries. It is home to an incredible diversity of plant and animal species, many of which are unique to the region. Deforestation and climate change pose significant threats to its continued existence.'
Summary: The Amazon rainforest, the world's largest, is a biodiversity hotspot facing severe threats from deforestation and climate change.

Paragraph: 'The invention of the printing press by Johannes Gutenberg in the 15th century revolutionized the dissemination of knowledge. It made books and other printed materials more widely available and affordable, leading to increased literacy and the spread of new ideas across Europe.'
Summary: Johannes Gutenberg's 15th-century printing press revolutionized knowledge dissemination by making printed materials more accessible and fostering literacy.

Paragraph: 'Artificial intelligence (AI) is a rapidly developing field of computer science that aims to create machines capable of performing tasks that typically require human intelligence. This includes learning, problem-solving, decision-making, and understanding language. AI has applications in various sectors, from healthcare to finance.'
Summary:
""",
"""Correct the grammatical errors in the following sentences:

Sentence: 'She don't like coffee.'
Corrected: 'She doesn't like coffee.'

Sentence: 'The cat jump on the table.'
Corrected: 'The cat jumped on the table.'

Sentence: 'Me and him went to the store.'
Corrected: 'He and I went to the store.'

Sentence: 'Their is a dog in the yard.'
Corrected:
"""
]

