from server import mcp
from TM1py import TM1Service
from config import TM1_CONFIG
from typing import List, Dict

@mcp.tool()
def get_all_dimensions() -> List[str]:
    """Get all dimensions names from TM1"""
    
    with TM1Service(**TM1_CONFIG) as tm1:
        dimensions = tm1.dimensions.get_all_names()
        return [dimension for dimension in dimensions]

@mcp.tool()
def get_model_dimensions() -> List[str]:
    """Get all model dimensions (skipping control dimensions) from TM1"""
    
    with TM1Service(**TM1_CONFIG) as tm1:
        dimensions = tm1.dimensions.get_all_names(skip_control_dims=True)
        return [dimension for dimension in dimensions]

@mcp.tool()
def get_dimension_count(skip_control_dims: bool = False) -> int:
    """Get total number of dimensions in TM1
    
    Args:
        skip_control_dims: Set to True to exclude control dimensions
    """
    
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.dimensions.get_number_of_dimensions(skip_control_dims=skip_control_dims)

@mcp.tool()
def dimension_exists(dimension_name: str) -> bool:
    """Check if a dimension exists in TM1
    
    Args:
        dimension_name: Name of the dimension to check
    """
    
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.dimensions.exists(dimension_name)

@mcp.tool()
def get_dimension(dimension_name: str) -> Dict:
    """Get a dimension's details from TM1
    
    Args:
        dimension_name: Name of the dimension to retrieve
    """
    
    with TM1Service(**TM1_CONFIG) as tm1:
        dimension = tm1.dimensions.get(dimension_name)
        return dimension.body_as_dict

@mcp.tool()
def execute_dimension_mdx(dimension_name: str, mdx: str) -> List[str]:
    """Execute MDX against a dimension
    
    Args:
        dimension_name: Name of the dimension
        mdx: Valid MDX statement for the dimension
    
    Returns:
        List of element names
    """
    
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.dimensions.execute_mdx(dimension_name, mdx)