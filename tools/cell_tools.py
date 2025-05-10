from server import mcp
from TM1py import TM1Service
from config import TM1_CONFIG
import pandas as pd
from typing import Iterable, Union, List, Dict, Tuple, Optional, Any

@mcp.tool()
def get_value(cube_name: str, elements: Union[str, Iterable]) -> Union[str, float]:
    """Get the value of a specific intersection in a cube
    
    Args:
        cube_name: Name of the cube
        elements: string of elements separated by comma or an iterable of element names representing the intersection
        
    Returns:
        Cell value at the specified intersection
    """
    
    with TM1Service(**TM1_CONFIG) as tm1:
        value = tm1.cells.get_value(cube_name=cube_name, elements=elements)
        return value