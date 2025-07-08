# LangChain MCP Example

This is an example project demonstrating how to use **LangChain MCP Adapters**, **LangGraph**, and **Groq API** to create a multi-server tool agent. The client connects to two servers:
- A Math server (local Python process using stdio transport)
- A Weather server (local HTTP server)

## ✅ Requirements

- Python 3.9+
- The following Python packages:
  - `langchain`
  - `langchain-mcp-adapters`
  - `langgraph`
  - `langchain-groq`
  - `mcp`
  - `python-dotenv`

Install dependencies using:

```bash
uv pip install -r requirements.txt




⚙️ Example Output
Math response: The answer is 96.
Weather response: The weather in California is sunny with a high of 27°C.




🔍 Troubleshooting
ModuleNotFoundError: Ensure all dependencies are installed.

CancelledError: Make sure the servers are running before the client.

'args' parameter is required: Ensure that your math server connection is correctly configured with "args" in the client.py.





🛠️ Built With
LangChain MCP Adapters

LangGraph

Groq API
