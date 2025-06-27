# Prompt Engineering Patterns & Grounding Implementation

Python implementation task to master prompt engineering patterns and grounding techniques using DIAL API for AI-powered applications.

## 🎓 Learning Goals

By completing this task, you will learn:
- **8 Essential Prompting Patterns**: Zero-shot, One-shot, Few-shot, Chain-of-thought, Role-based, Persona, Constraint, and Template patterns
- **Grounding Fundamentals**: How to implement Retrieval-Augmented Generation (RAG) for factual accuracy

## 📋 Requirements

- Python 3.11+
- EPAM VPN connection (for DIAL API access)
- API key for DIAL service

## 🔧 Setup

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Set your API key:**
    - Ensure you are connected to the EPAM VPN
    - Get the DIAL API key here: https://support.epam.com/ess?id=sc_cat_item&table=sc_cat_item&sys_id=910603f1c3789e907509583bb001310c

3. **Project structure:**
   ```
   tasks/
   ├── _constants.py                        # ✅ API configuration
   ├── prompting/
   │   ├── t_1_zero_shot.py                 # 🚧 TODO - Zero-shot prompts
   │   ├── t_2_one_shot.py                  # 🚧 TODO - One-shot prompts
   │   ├── t_3_few_shot.py                  # 🚧 TODO - Few-shot prompts
   │   ├── t_4_chain_of_thought.py          # 🚧 TODO - Chain-of-thought prompts
   │   ├── t_5_role_based.py                # 🚧 TODO - Role-based prompts
   │   ├── t_6_persona_pattern.py           # 🚧 TODO - Persona pattern prompts
   │   ├── t_7_constraint_pattern.py        # 🚧 TODO - Constraint pattern prompts
   │   └── t_8_template_pattern.py          # 🚧 TODO - Template pattern prompts
   └── grounding/
       └── task.py                          # 🚧 TODO - Grounding implementation
   tests/
   ├── prompting/                           # ✅ Pattern validation tests
   └── grounding/                           # ✅ Grounding validation tests
   ```

## 🎯 Your Tasks

### Part 1: Prompting Patterns (8 Tasks)

Complete each prompting pattern by implementing **at least 2 prompts** for each pattern:

#### 🔸 **Task 1: Zero-Shot Pattern** [t_1_zero_shot.py](tasks/prompting/t_1_zero_shot.py). Test: [test_1_zero_shot.py](tests/prompting/test_1_zero_shot.py).
#### 🔸 **Task 2: One-Shot Pattern** [t_2_one_shot.py](tasks/prompting/t_2_one_shot.py). Test: [test_2_one_shot.py](tests/prompting/test_2_one_shot.py).
#### 🔸 **Task 3: Few-Shot Pattern** [t_3_few_shot.py](tasks/prompting/t_3_few_shot.py). Test: [test_3_few_shot.py](tests/prompting/test_3_few_shot.py).
#### 🔸 **Task 4: Chain-of-Thought Pattern** [t_4_chain_of_thought.py](tasks/prompting/t_4_chain_of_thought.py). Test: [test_4_chain_of_thought.py](tests/prompting/test_4_chain_of_thought.py).
#### 🔸 **Task 5: Role-Based Pattern** [t_5_role_based.py](tasks/prompting/t_5_role_based.py). Test: [test_5_role_based.py](tests/prompting/test_5_role_based.py).
#### 🔸 **Task 6: Persona Pattern** [t_6_persona_pattern.py](tasks/prompting/t_6_persona_pattern.py). Test: [test_6_persona_pattern.py](tests/prompting/test_6_persona_pattern.py).
#### 🔸 **Task 7: Constraint Pattern** [t_7_constraint_pattern.py](tasks/prompting/t_7_constraint_pattern.py). Test: [test_7_constraint_pattern.py](tests/prompting/test_7_constraint_pattern.py).
#### 🔸 **Task 8: Template Pattern** [t_8_template_pattern.py](tasks/prompting/t_8_template_pattern.py). Test: [test_8_template_pattern.py](tests/prompting/test_8_template_pattern.py).

### Part 2: Grounding Implementation [task.py](tasks/grounding/task.py). Test: [test_grounding.py](tests/grounding/test_grounding.py).

### Understanding Test Output

**For Prompting Patterns:**
- ✅ **No manipulation detected**: Your prompt passes safety checks
- ✅ **Pattern validation passed**: Your prompt correctly follows the pattern
- 📝 **Response**: Shows the AI's response to your prompt
- ❌ **Validation failed**: Shows specific issues to fix

**For Grounding:**
- ✅ **No manipulation detected**: System prompt passes safety checks
- 🔗 **Augmented prompt**: Shows the formatted prompt with retrieved context
- 🤖 **Response**: Shows the AI's grounded response
- ✅ **Grounding validation passed**: Context was properly retrieved and used


## 🛠️ Implementation Tips

### Prompting Patterns Best Practices

1. **Be Specific**: Use clear, actionable language
2. **Follow Format**: Each pattern has specific structural requirements
3. **Avoid Manipulation**: Don't include phrases like "this is crucial for my grade"
4. **Test Iteratively**: Run tests frequently to catch issues early
5. **Read Validation Messages**: Error messages provide specific guidance

### Grounding Implementation Tips

1. **Study the Context**: Understand the provided knowledge base content
2. **XML Formatting**: Use proper `<context>` and `<user_question>` tags
3. **Placeholder Syntax**: Use `{context}` and `{user_question}` for substitution
4. **System Instructions**: Be clear about using only provided context
5. **Error Handling**: Consider cases where context is insufficient

### Common Pitfalls

**Prompting:**
- ❌ Mixing patterns (e.g., adding examples to zero-shot)
- ❌ Vague constraints that can't be measured
- ❌ Templates without rigid structure
- ❌ Roles without detailed personas

**Grounding:**
- ❌ Forgetting to implement required methods
- ❌ Incorrect API configuration
- ❌ Missing XML formatting in prompts
- ❌ Not restricting to provided context

---

# <img src="dialx-banner.png">