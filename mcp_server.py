# server.py
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")


# Add an addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print(f"Adding {a} and {b}")
    return a + b


@mcp.resource("resource://static_data")
def get_static_resource() -> str:
    """Static resource data"""
    return "This is a static text"


@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get the personlized greeting"""
    return f"Hello, {name}!"


@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"


@mcp.prompt()
def debug_error(error: str) -> list[tuple]:
    return [
        ("user", "I'm seeing this error"),
        ("user", error),
        ("assistant", "I'll help debug that. What have you tried so far?"),
    ]


if __name__ == "__main__":
    mcp.run(transport="sse")
