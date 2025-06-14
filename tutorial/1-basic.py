from langgraph.prebuilt import create_react_agent
from langchain.chat_models import init_chat_model
from langgraph.checkpoint.memory import InMemorySaver
from pydantic import BaseModel

from dotenv import load_dotenv

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))
from config import models

load_dotenv()

def get_weather(city: str) -> str:  
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"


class WeatherResponse(BaseModel):
    conditions: str



checkpointer = InMemorySaver()

model = init_chat_model(
    models.HAIKU3,
    temperature=0
)

agent = create_react_agent(
    model=model,
    tools=[get_weather],  
    prompt="You are a helpful assistant",
    checkpointer=checkpointer,
    response_format=WeatherResponse
)

config = {"configurable": {"thread_id": "1"}}
sf_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]},
    config  
)
ny_response = agent.invoke(
    {"messages": [{"role": "user", "content": "what about new york?"}]},
    config
)

# print(ny_response)
print(config)


# conditions='Sunny and mild'
sf_response["structured_response"]

