---
name: write-task-prompt
description: Convert a user's described task into a clear, standalone, ready-to-use prompt and return that prompt inside one fenced code block. Use when the user asks to create, write, improve, or package a prompt that will instruct another AI or agent to perform the described work, especially when they want only the prompt or want it wrapped in triple backticks.
---

# Write Task Prompt

Turn the user's request into a prompt for another capable AI or agent. Create the prompt; do not perform the underlying task.

## Build the prompt

1. Infer the intended task, audience, available context, constraints, deliverables, and success criteria from the conversation.
2. Preserve concrete names, paths, technologies, formats, limits, and user preferences exactly.
3. Resolve minor gaps with conservative, useful defaults. Include a request for clarification inside the generated prompt only when proceeding would be unsafe or would materially change the result.
4. Make the prompt standalone. Include all relevant context from the conversation so its recipient does not need the original chat.
5. Tell the recipient to:
   - inspect relevant inputs before acting;
   - preserve existing work and avoid unrelated changes when files or code are involved;
   - state important assumptions;
   - complete the task rather than merely describe steps, unless the user asked for analysis or a plan;
   - verify the result in proportion to risk;
   - report the outcome, validation, and unresolved limits concisely.
6. Match the user's language unless they request another language.
7. Prefer direct instructions and useful structure. Omit generic persona text, motivational filler, repeated requirements, and invented details.

## Output contract

- Return exactly one fenced code block containing only the generated prompt.
- Add no introduction, explanation, label, or text outside the fence.
- Use triple backticks by default.
- If the generated prompt itself contains triple backticks, wrap it with a longer backtick fence so the block remains valid.
- Do not use a language tag unless the user requests one.
