from server import mcp
from TM1py import TM1Service
from config import TM1_CONFIG


@mcp.tool()
def get_all_cubes() -> list:
    """Get all cubes from TM1"""
    
    with TM1Service(**TM1_CONFIG) as tm1:
        cubes = tm1.cubes.get_all()
        return [cube.name for cube in cubes]