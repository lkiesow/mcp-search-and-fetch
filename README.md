# MCP Search & Fetch

An MCP server exposing Ollama's web search and web fetch capabilities as tools.

## Features

- **web_search**: Perform web searches using Ollama's hosted search API
- **web_fetch**: Fetch content from web pages

## Requirements

- Ollama API key ([get one from ollama.com](https://ollama.com/login))

## Installation

```bash
# Clone the repository
git clone <repo-url>
cd mcp-search-and-fetch

# Install dependencies
pip install -r requirements.txt

# Copy environment sample
cp .env.sample .env
```

Edit `.env` with your Ollama API key:

```
OLLAMA_API_KEY=your_api_key_here
```

## Usage

### Local (stdio)

```bash
python web-search-mcp.py
```

### HTTP Server

```bash
# Set port and host in .env
export MCP_SERVER_PORT=8000
export MCP_SERVER_HOST=0.0.0.0

python web-search-mcp.py
```

### Docker

```bash
docker build -t mcp-search-fetch .
docker run -p 8000:8000 --env-file .env mcp-search-fetch
```

## Configuration

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
