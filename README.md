# MCP Search & Fetch

An MCP server exposing Ollama's web search and web fetch capabilities as tools.

## Features

- **web_search**: Perform web searches using Ollama's hosted search API
- **web_fetch**: Fetch content from web pages

## Requirements

- Ollama API key ([get one from ollama.com](https://ollama.com/login))

## Installation

```bash
pip install mcp-search-and-fetch

# Export your API key
OLLAMA_API_KEY=your_api_key_here

# Run the MCP server
mcp-search-and-fetch
```

## Clone from Repository

```bash
# Clone the repository
git clone https://github.com/lkiesow/mcp-search-and-fetch.git
cd mcp-search-and-fetch

# Install dependencies
pip install -r requirements.txt

export OLLAMA_API_KEY=your_api_key_here
python mcp_search_and_fetch.py
```

## Usage

### Local (stdio)

```bash
python mcp_search_and_fetch.py
```

### HTTP Server (Streamable HTTP)

```bash
# Set port and host in .env
export MCP_SERVER_PORT=8000
export MCP_SERVER_HOST=0.0.0.0

python mcp_search_and_fetch.py
```

### Docker

```bash
docker build -t mcp-search-fetch .
docker run -p 8000:8000 --env-file .env mcp-search-fetch
```

## Configuration

You can either set environment variables or provide a `.env` file.
Take a look at the [.env.sample](.env.sample) for an example.

| Environment Variable | Required | Default   | Description
|----------------------|----------|-----------|------------------------------
| `OLLAMA_API_KEY`     | Yes      | -         | Your Ollama API key
| `MCP_SERVER_PORT`    | No       | -         | Run HTTP server on specified port
| `MCP_SERVER_HOST`    | No       | 127.0.0.1 | Host to bind to

## Tools

### web_search(query, max_results=3)

Performs a web search and returns results as JSON.

### web_fetch(url)

Fetches content from a URL and returns it as JSON.
