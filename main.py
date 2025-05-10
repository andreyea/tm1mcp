# main.py
from server import mcp

# Import tools to register them in the MCP server
import tools.cube_tools
import tools.cell_tools
import tools.mdx_tools
import tools.dimension_tools

if __name__ == "__main__":
    mcp.run()