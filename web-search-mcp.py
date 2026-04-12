#!/usr/bin/env python3

"""
MCP server exposing Ollama web_search and web_fetch as tools.

Environment:
- OLLAMA_API_KEY (required): if set, will be used as Authorization header.
"""

import os

from fastmcp import FastMCP
from ollama import Client

client = Client(
    host="https://ollama.com",
    headers={"Authorization": "Bearer " + os.getenv("OLLAMA_API_KEY", "")},
)

mcp = FastMCP("ollama-search-fetch")


@mcp.tool
def web_search(query: str, max_results: int = 3) -> dict:
    """
    Perform a web search using Ollama's hosted search API.

    Args:
      query: The search query to run.
      max_results: Maximum results to return (default: 3).

    Returns:
      JSON-serializable dict matching ollama.WebSearchResponse.model_dump()
    """
    res = client.web_search(query=query, max_results=max_results)
    return res.model_dump()


@mcp.tool
def web_fetch(url: str) -> dict:
    """
    Fetch the content of a web page for the provided URL.

    Args:
      url: The absolute URL to fetch.

    Returns:
      JSON-serializable dict matching ollama.WebFetchResponse.model_dump()
    """
    res = client.web_fetch(url=url)
    return res.model_dump()


if __name__ == "__main__":
    mcp.run()
