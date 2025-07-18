# general_instructions.md

This document provides unified onboarding and workflow guidance for all contributors and agents working on the iOS LLM project.

## Key Instruction Files

- **GEMINI.md** — Agent workflow, planning, and execution protocol.
- **.github** — System prompt and agent behavior for implementation planning.
- **.instructions/** — Language/platform-specific best practices (e.g., python_best_practices.md, swift_best_practices.md).
- **.research/** — All experiment logs, findings, and failed attempts must be documented here.
- **.issue/** — Issue-specific plans, environment tracking, and research for reproducibility.

## General Best Practices

- Always follow the best practices in `.instructions/` for your language or platform.
- Never hardcode secrets, credentials, or environment-specific values—use configuration files or environment variables.
- Use structured error handling and provide clear, actionable error messages.
- Organize code and assets by feature or layer.
- Write and maintain unit/integration tests for all critical logic.
- Document all experiments, findings, and failures in `.research/`.
- Use descriptive names and keep documentation up to date.
- If requirements are unclear, ask clarifying questions before proceeding.

## iOS/LLM Project Focus

- All instructions and workflows are for an iOS app that runs an LLM model locally.
- Remove any references to Eurovision, Flutter, or unrelated technologies.

For onboarding, workflow, or code style, always start with this file and follow the links to the relevant detailed instructions.
