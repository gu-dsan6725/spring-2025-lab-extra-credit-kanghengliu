"""
Google Search MCP Server

This server provides MCP tools to interact with Google Search API.
"""

from collections import defaultdict
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Union

import pandas as pd
import requests
from bs4 import BeautifulSoup
from googlesearch import search
from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field
from tabulate import tabulate

# Initialize FastMCP server
mcp = FastMCP("google_search")


@mcp.tool()
async def query_google_top_results(params: str) -> list:
    """
    Perform a Google Search query and return the top results.

    Args:
        params: The query string to search for.

    Returns:
        A list of top search URLs.
    """
    results = list(search(params))
    return results


@mcp.tool()
async def parse_google_html(params: str) -> str:
    """
    Retrieve content from a URL of a google search results.

    Args:
        params: The URL of the Google search result.

    Returns:
        The parsed HTML content.
    """
    response = requests.get(params, timeout=10)
    soup = BeautifulSoup(response.text, "html.parser")
    page_text = soup.get_text(separator="\n", strip=True)
    return page_text


def main():
    # Run the server with SSE transport
    mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
