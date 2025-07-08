from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv

import asyncio
import os

load_dotenv()

async def main():
    client = MultiServerMCPClient(
        connections={
            "math": {
                "command": "python",
                "args": ["mathserver.py"],  # Ensure the path is correct
                "transport": "stdio",
            }
        }
    )

    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="qwen-qwq-32b")

    agent = create_react_agent(
        model,
        tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "what's (3 + 5) x 12?"}]}
    )

    print("Math response:", math_response['messages'][-1].content)

asyncio.run(main())
