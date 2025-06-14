from typing import Annotated

from langchain_tavily import TavilySearch
from langchain_core.messages import BaseMessage
from typing_extensions import TypedDict

from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langgraph.checkpoint.memory import MemorySaver


import os
from langchain.chat_models import init_chat_model

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



def chatbot(state: State):
    return {"messages": [llm.invoke(state["messages"])]}

graph_builder.add_node("chatbot", chatbot)


graph_builder.add_edge(START, "chatbot")
graph = graph_builder.compile(checkpointer=memory)

response = graph.invoke(
    {"messages": [{"role": "user", "content": 'My name is Will.'}]},
    config
    )

response["messages"][-1].pretty_print()

response = graph.invoke(
    {"messages": [{"role": "user", "content": 'Remember my name?'}]},
    config
    )
response["messages"][-1].pretty_print()