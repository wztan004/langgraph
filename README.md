# Commands
`poetry env activate`
`python -m tutorial.1-basic`

# Learnings
- `tools_condition`: route to the ToolNode if the last message has tool calls.
- `add_conditional_edges`: optionally route to 1 or more edges (or optionally terminate)
- `interrupt`: for human in the loop input
- `update_state`: override values of state keys
- Time Travel: start from a previous response and explore a different outcome

# Good features
- [Structured output](https://langchain-ai.github.io/langgraph/agents/agents/#6-configure-structured-output)

# Core Concepts
- `StateGraph`: state machine
- `Nodes`: units of work

# Models
https://docs.anthropic.com/en/docs/about-claude/models/overview