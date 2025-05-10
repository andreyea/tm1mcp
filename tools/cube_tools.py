from server import mcp
from TM1py import TM1Service
from config import TM1_CONFIG


@mcp.tool()
def get_all_cubes() -> list:
    """Get all cubes from TM1"""
    
    with TM1Service(**TM1_CONFIG) as tm1:
        cubes = tm1.cubes.get_all()
        return [cube.name for cube in cubes]


@mcp.tool()
def get_cube_names(skip_control_cubes: bool = False) -> list:
    """Get names of all cubes from TM1
    
    Args:
        skip_control_cubes: If True, excludes control cubes (with } prefix)
        
    Returns:
        List of cube names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.get_all_names(skip_control_cubes=skip_control_cubes)


@mcp.tool()
def get_cube_details(cube_name: str) -> dict:
    """Get detailed information about a specific cube
    
    Args:
        cube_name: Name of the cube
        
    Returns:
        Dictionary with cube details
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        if not tm1.cubes.exists(cube_name=cube_name):
            return {"error": f"Cube '{cube_name}' does not exist"}
            
        cube = tm1.cubes.get(cube_name=cube_name)
        dimension_names = tm1.cubes.get_dimension_names(cube_name=cube_name)
        
        try:
            last_update = tm1.cubes.get_last_data_update(cube_name=cube_name)
        except:
            last_update = "Unknown"
            
        return {
            "name": cube.name,
            "dimensions": dimension_names,
            "rules": cube.rules if hasattr(cube, 'rules') else None,
            "last_data_update": last_update
        }


@mcp.tool()
def check_cube_exists(cube_name: str) -> bool:
    """Check if a cube exists in TM1
    
    Args:
        cube_name: Name of the cube to check
        
    Returns:
        Boolean indicating whether the cube exists
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.exists(cube_name=cube_name)


@mcp.tool()
def get_cube_dimensions(cube_name: str) -> list:
    """Get dimensions of a specific cube in their correct order
    
    Args:
        cube_name: Name of the cube
        
    Returns:
        List of dimension names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        if not tm1.cubes.exists(cube_name=cube_name):
            return []
        return tm1.cubes.get_dimension_names(cube_name=cube_name)


@mcp.tool()
def find_cubes_with_dimension(dimension_name: str, skip_control_cubes: bool = False) -> list:
    """Find cubes that contain a specific dimension
    
    Args:
        dimension_name: Name of the dimension to search for
        skip_control_cubes: If True, excludes control cubes from search
        
    Returns:
        List of cube names containing the dimension
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.search_for_dimension(dimension_name=dimension_name, 
                                             skip_control_cubes=skip_control_cubes)


@mcp.tool()
def get_cubes_with_rules(skip_control_cubes: bool = False) -> list:
    """Get names of cubes that have rules
    
    Args:
        skip_control_cubes: If True, excludes control cubes
        
    Returns:
        List of cube names that have rules
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.get_all_names_with_rules(skip_control_cubes=skip_control_cubes)


@mcp.tool()
def check_cube_rules(cube_name: str) -> list:
    """Check rules syntax for a cube
    
    Args:
        cube_name: Name of the cube
        
    Returns:
        List of errors (empty if no errors found)
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        if not tm1.cubes.exists(cube_name=cube_name):
            return [f"Cube '{cube_name}' does not exist"]
        return tm1.cubes.check_rules(cube_name=cube_name)


@mcp.tool()
def find_cubes_with_rule_text(substring: str, skip_control_cubes: bool = False) -> list:
    """Find cubes that contain specific text in their rules
    
    Args:
        substring: Text to search for in rules
        skip_control_cubes: If True, excludes control cubes from search
        
    Returns:
        List of cube names that have matching rule text
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        cubes = tm1.cubes.search_for_rule_substring(
            substring=substring,
            skip_control_cubes=skip_control_cubes
        )
        return [cube.name for cube in cubes]


@mcp.tool()
def get_model_cubes() -> list:
    """Get all cubes without } prefix (model cubes)
    
    Returns:
        List of model cube names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        model_cubes = tm1.cubes.get_model_cubes()
        return [cube.name for cube in model_cubes]


@mcp.tool()
def get_control_cubes() -> list:
    """Get all cubes with } prefix (control cubes)
    
    Returns:
        List of control cube names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        control_cubes = tm1.cubes.get_control_cubes()
        return [cube.name for cube in control_cubes]


@mcp.tool()
def get_cube_count(skip_control_cubes: bool = False) -> int:
    """Get the total number of cubes in TM1
    
    Args:
        skip_control_cubes: If True, excludes control cubes from count
        
    Returns:
        Count of cubes
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.get_number_of_cubes(skip_control_cubes=skip_control_cubes)


@mcp.tool()
def get_cubes_without_rules(skip_control_cubes: bool = False) -> list:
    """Get names of cubes that do not have rules
    
    Args:
        skip_control_cubes: If True, excludes control cubes
        
    Returns:
        List of cube names without rules
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.get_all_names_without_rules(skip_control_cubes=skip_control_cubes)


@mcp.tool()
def find_dimensions_with_substring(substring: str, skip_control_cubes: bool = False) -> dict:
    """Find cubes containing dimensions that match a substring
    
    Args:
        substring: Text to search for in dimension names
        skip_control_cubes: If True, excludes control cubes from search
        
    Returns:
        Dictionary with cube names as keys and matching dimensions as values
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.cubes.search_for_dimension_substring(
            substring=substring,
            skip_control_cubes=skip_control_cubes
        )


@mcp.tool()
def get_measure_dimension(cube_name: str) -> str:
    """Get the measure dimension (last dimension) of a cube
    
    Args:
        cube_name: Name of the cube
        
    Returns:
        Name of the measure dimension
    """
    try:
        with TM1Service(**TM1_CONFIG) as tm1:
            if not tm1.cubes.exists(cube_name=cube_name):
                return ""
            
            return tm1.cubes.get_measure_dimension(cube_name=cube_name)
    except Exception as e:
        return ""
