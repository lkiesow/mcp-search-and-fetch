FROM python:3.14-slim

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY mcp_search_and_fetch.py .

# Create non-root user for security
RUN useradd -m -u 1000 searchandfetch && chown -R searchandfetch:searchandfetch /app
USER searchandfetch

# Set default environment variables for MCP server
ENV MCP_SERVER_PORT=8000
ENV MCP_SERVER_HOST=0.0.0.0

# Expose port
EXPOSE 8000

# Run the MCP server
CMD ["python", "mcp_search_and_fetch.py"]
