# `get_state_history`: replay the message history

from typing import Annotated
from typing_extensions import TypedDict

from langchain_tavily import TavilySearch
from langchain_core.messages import BaseMessage, ToolMessage
from langchain_core.tools import InjectedToolCallId, tool
from langchain.chat_models import init_chat_model

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver
from langgraph.types import Command, interrupt

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import models
from dotenv import load_dotenv


load_dotenv()
llm = init_chat_model(models.HAIKU3)
config = {"configurable": {"thread_id": "1"}}
memory = MemorySaver()

class State(TypedDict):
    messages: Annotated[list, add_messages]



# TOOLS
tool = TavilySearch(max_results=2)
tools = [tool]
llm_with_tools = llm.bind_tools(tools)



# GRAPH BUILDING
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_edge("tools", "chatbot")
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile(checkpointer=memory)



# RESPONSES
user_input = (
    "I'm learning LangGraph."
    "Could you do some research on it for me?"
)

response = graph.invoke(
    {"messages": [{"role": "user", "content": user_input}]},
    config
    )

user_input = (
    "Ya that's helpful. Maybe I'll "
    "build an autonomous agent with it!"
)

response = graph.invoke(
    {"messages": [{"role": "user", "content": user_input}]},
    config
    )

for r in response["messages"]:
    r.pretty_print()



to_replay = None
for state in graph.get_state_history(config):
    print("Num Messages: ", len(state.values["messages"]), "Next: ", state.next)
    print("-" * 80)
    if len(state.values["messages"]) == 5:
        # We are somewhat arbitrarily selecting a specific state based on the number of chat messages in the state.
        to_replay = state

print('------')
responses = graph.invoke(None, to_replay.config)


responses['messages'][-1].pretty_print()