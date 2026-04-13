#!/usr/bin/env python3

"""
Simple FastMCP client test script for the ollama-search-fetch MCP server.

This client connects to the MCP server using stdio transport and demonstrates
calling the available tools (web_search and web_fetch).
"""

import asyncio

from fastmcp import Client
from fastmcp.client.transports import StdioTransport


async def main():
    # Create stdio transport to run the server as a subprocess
    transport = StdioTransport(command="python", args=["mcp_search_and_fetch.py"])

    # Create the client with the transport
    client = Client(transport)

    # Use the client with async context manager
    async with client:
        print("Connected to MCP server!")
        print()

        # List available tools
        tools = await client.list_tools()
        print("Available tools:")
        for tool in tools:
            print(f"  - {tool.name}: {str(tool.description)[:40]}…")
        print()

        # Test web_search tool
        print("Testing web_search tool...")
        search_result = await client.call_tool(
            "web_search", {"query": "FastMCP documentation", "max_results": 2}
        )
        print(f"Search result: {str(search_result)[:40]}…")
        print()

        # Test web_fetch tool
        print("Testing web_fetch tool...")
        fetch_result = await client.call_tool(
            "web_fetch", {"url": "https://lkiesow.de"}
        )
        print(f"Fetch result: {str(fetch_result)[:40]}…")
        print()

        print("All tests completed!")


if __name__ == "__main__":
    asyncio.run(main())
