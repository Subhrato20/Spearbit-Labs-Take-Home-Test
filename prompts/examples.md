# Hackmerlin.io Puzzle Examples

This file contains examples of different types of puzzles you might encounter on hackmerlin.io to help guide the AI agent's responses.

## Example 1: Uppercase Single Token Puzzle

**Puzzle:** "What is the opposite of 'down'? Answer in UPPERCASE."

**Correct Response:** "UP"

**Explanation:** The puzzle asks for the opposite of "down" and specifically requests UPPERCASE formatting. The answer should be exactly one word in all caps.

## Example 2: Yes/No Question

**Puzzle:** "Is the sky blue during the day? Answer YES or NO."

**Correct Response:** "YES"

**Explanation:** This is a straightforward yes/no question. The response should be exactly "YES" or "NO" in uppercase, matching the format requested.

## Example 3: Multiple Choice Click

**Puzzle:** "Which of these is a programming language? Click the correct answer:
- A) Python
- B) Carrot
- C) Mountain
- D) Ocean"

**Correct Response:** Click on option A (Python)

**Explanation:** The agent should identify that Python is a programming language and click on that option. The other options are not programming languages.

## Example 4: One-Token Answer with Retry

**Puzzle:** "What do you call a baby cow? Give me ONE TOKEN."

**First Attempt:** "calf"

**Feedback:** "Please use UPPERCASE for your answer."

**Correct Response:** "CALF"

**Explanation:** The puzzle asks for one token (word) and the feedback indicates uppercase is required. The agent should retry with the correct formatting.

## Example 5: Mathematical Puzzle

**Puzzle:** "What is 2 + 2? Answer in UPPERCASE."

**Correct Response:** "FOUR"

**Explanation:** Simple mathematical question requiring the answer in uppercase format.

## Example 6: Pattern Recognition

**Puzzle:** "Complete the sequence: A, B, C, ? Answer in UPPERCASE."

**Correct Response:** "D"

**Explanation:** The sequence follows the alphabet. The next letter after C is D, and it should be in uppercase as requested.

## Key Patterns to Remember:

1. **UPPERCASE requirement** - Always check if the puzzle asks for uppercase answers
2. **One-token answers** - Provide exactly one word when asked for "one token"
3. **Yes/No format** - Use exactly "YES" or "NO" for yes/no questions
4. **Retry on format errors** - If feedback mentions formatting, try again with correct format
5. **Click for multiple choice** - Identify the correct option and click it
6. **Think step by step** - Break down complex puzzles into smaller parts
