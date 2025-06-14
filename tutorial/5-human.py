# `interrupt`: Pauses execution at a specific point, presents information for human review.
# `command`: Used to resume execution with a value provided by the human.

from typing import Annotated
from typing_extensions import TypedDict

from langchain_tavily import TavilySearch
from langchain_core.messages import BaseMessage
from langchain_core.tools import tool
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

graph_builder = StateGraph(State)



# TOOLS
@tool
def human_assistance(query: str) -> str:
    """Request assistance from a human."""
    human_response = interrupt({"query": query})
    return human_response["data"]

tools = [human_assistance]
llm_with_tools = llm.bind_tools(tools)



# GRAPH BUILDING
def chatbot(state: State):
    return {"messages": [llm_with_tools.invoke(state["messages"])]}

tool_node = ToolNode(tools=tools)
graph_builder.add_node("tools", tool_node)
graph_builder.add_conditional_edges(
    "chatbot",
    tools_condition,
)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile(checkpointer=memory)



# RESPONSES
response = graph.invoke(
    {"messages": [{"role": "user", "content": 'I need some expert guidance for building an AI agent. Could you request assistance for me?'}]},
    config
    )

response["messages"][-1].pretty_print()
snapshot = graph.get_state(config)
print(snapshot.next)



human_response = (
    "We, the experts are here to help! We'd recommend you check out LangGraph to build your agent."
    " It's much more reliable and extensible than simple autonomous agents."
)

human_command = Command(resume={"data": human_response})
response = graph.invoke(
    human_command,
    config
    )
response["messages"][-1].pretty_print()