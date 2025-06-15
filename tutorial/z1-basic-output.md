
sf_response["structured_response"]
```
conditions='Sunny and mild'
```

config
```
{'configurable': {'thread_id': '1'}}
```


ny_response
```
{
  "messages": [
    {
      "content": "what is the weather in sf",
      "additional_kwargs": {},
      "response_metadata": {},
      "id": "f0f508b4-121a-4c96-a091-cf381122e073"
    },
    {
      "content": [
        {
          "id": "toolu_01CNxrKijucUKXrx9Q6TDYLK",
          "input": {
            "city": "sf"
          },
          "name": "get_weather",
          "type": "tool_use"
        }
      ],
      "additional_kwargs": {},
      "response_metadata": {
        "id": "msg_011egk7rQnGfvPgb518L9pRH",
        "model": "claude-3-haiku-20240307",
        "stop_reason": "tool_use",
        "stop_sequence": null,
        "usage": {
          "cache_creation_input_tokens": 0,
          "cache_read_input_tokens": 0,
          "input_tokens": 337,
          "output_tokens": 53,
          "server_tool_use": null,
          "service_tier": "standard"
        },
        "model_name": "claude-3-haiku-20240307"
      },
      "id": "run--30a78748-598a-48ee-8bd2-75fc0b28c2c0-0",
      "tool_calls": [
        {
          "name": "get_weather",
          "args": {
            "city": "sf"
          },
          "id": "toolu_01CNxrKijucUKXrx9Q6TDYLK",
          "type": "tool_call"
        }
      ],
      "usage_metadata": {
        "input_tokens": 337,
        "output_tokens": 53,
        "total_tokens": 390,
        "input_token_details": {
          "cache_creation": 0,
          "cache_read": 0
        }
      }
    },
    {
      "content": "It's always sunny in sf!",
      "name": "get_weather",
      "id": "1ef84477-3e5d-4cc8-8116-f8d26fbd86ca",
      "tool_call_id": "toolu_01CNxrKijucUKXrx9Q6TDYLK"
    },
    {
      "content": "The weather in San Francisco is generally mild and sunny. San Francisco has a Mediterranean climate, with cool, dry summers and mild, wet winters. The average high temperature in San Francisco is around 65°F (18°C) year-round, with the warmest months being September and October. Fog is common, especially in the summer months, as the city is situated on a peninsula between the Pacific Ocean and San Francisco Bay.",
      "additional_kwargs": {},
      "response_metadata": {
        "id": "msg_01VBc5PGBfkysHUsxwiz4Qmx",
        "model": "claude-3-haiku-20240307",
        "stop_reason": "end_turn",
        "stop_sequence": null,
        "usage": {
          "cache_creation_input_tokens": 0,
          "cache_read_input_tokens": 0,
          "input_tokens": 408,
          "output_tokens": 93,
          "server_tool_use": null,
          "service_tier": "standard"
        },
        "model_name": "claude-3-haiku-20240307"
      },
      "id": "run--577ed940-6aaf-4d18-af3c-e1ad23229cd2-0",
      "usage_metadata": {
        "input_tokens": 408,
        "output_tokens": 93,
        "total_tokens": 501,
        "input_token_details": {
          "cache_creation": 0,
          "cache_read": 0
        }
      }
    },
    {
      "content": "what about new york?",
      "additional_kwargs": {},
      "response_metadata": {},
      "id": "60f5f070-c509-4c85-b561-a1a520912ca4"
    },
    {
      "content": [
        {
          "id": "toolu_017himbjo525nPcusMADw7DL",
          "input": {
            "city": "new york"
          },
          "name": "get_weather",
          "type": "tool_use"
        }
      ],
      "additional_kwargs": {},
      "response_metadata": {
        "id": "msg_01PRob5tf8TGLTvpBPZ7UwoZ",
        "model": "claude-3-haiku-20240307",
        "stop_reason": "tool_use",
        "stop_sequence": null,
        "usage": {
          "cache_creation_input_tokens": 0,
          "cache_read_input_tokens": 0,
          "input_tokens": 509,
          "output_tokens": 56,
          "server_tool_use": null,
          "service_tier": "standard"
        },
        "model_name": "claude-3-haiku-20240307"
      },
      "id": "run--36bfa4a7-7435-475a-88bc-b517b16e9b10-0",
      "tool_calls": [
        {
          "name": "get_weather",
          "args": {
            "city": "new york"
          },
          "id": "toolu_017himbjo525nPcusMADw7DL",
          "type": "tool_call"
        }
      ],
      "usage_metadata": {
        "input_tokens": 509,
        "output_tokens": 56,
        "total_tokens": 565,
        "input_token_details": {
          "cache_read": 0,
          "cache_creation": 0
        }
      }
    },
    {
      "content": "It's always sunny in new york!",
      "name": "get_weather",
      "id": "9937cb0d-e6a8-4591-bdc4-ddc59f06e9a2",
      "tool_call_id": "toolu_017himbjo525nPcusMADw7DL"
    },
    {
      "content": "New York City has a humid subtropical climate, with warm, humid summers and cold, wet winters. The average high temperature in New York ranges from around 40°F (4°C) in January to 84°F (29°C) in July. The city experiences four distinct seasons, with significant variation in weather conditions throughout the year. New York is known for its variable weather, with the potential for snowstorms, heat waves, and thunderstorms, especially during the transitional spring and fall seasons.",
      "additional_kwargs": {},
      "response_metadata": {
        "id": "msg_01DjATLh5FT8VTnaCBtFWJNb",
        "model": "claude-3-haiku-20240307",
        "stop_reason": "end_turn",
        "stop_sequence": null,
        "usage": {
          "cache_creation_input_tokens": 0,
          "cache_read_input_tokens": 0,
          "input_tokens": 582,
          "output_tokens": 110,
          "server_tool_use": null,
          "service_tier": "standard"
        },
        "model_name": "claude-3-haiku-20240307"
      },
      "id": "run--86fad2e5-1f30-452b-8905-e8401c0a5629-0",
      "usage_metadata": {
        "input_tokens": 582,
        "output_tokens": 110,
        "total_tokens": 692,
        "input_token_details": {
          "cache_read": 0,
          "cache_creation": 0
        }
      }
    }
  ],
  "structured_response": {
    "conditions": "Sunny"
  }
}
```