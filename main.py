# server.py
from mcp.server.fastmcp import FastMCP
from TM1py import TM1Service

# Create an MCP server
mcp = FastMCP("TM1")

@mcp.tool()
def get_all_cubes() -> list:
    """Get all cubes from TM1"""
    
    with TM1Service(address="localhost", port=8882, user="admin", password="", ssl=True) as tm1:
        cubes = tm1.cubes.get_all()
        return [cube.name for cube in cubes]