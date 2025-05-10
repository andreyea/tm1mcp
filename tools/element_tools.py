from server import mcp
from TM1py import TM1Service
from config import TM1_CONFIG
from typing import List, Dict, Optional, Union, Any, Tuple

@mcp.tool()
def get_element(dimension_name: str, hierarchy_name: str, element_name: str) -> Dict:
    """Get details for a specific element in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        element_name: Name of the element to retrieve
    
    Returns:
        Dictionary with element details
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        element = tm1.elements.get(dimension_name, hierarchy_name, element_name)
        return element.body_as_dict

@mcp.tool()
def get_elements(dimension_name: str, hierarchy_name: str) -> List[Dict]:
    """Get all elements in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
    
    Returns:
        List of elements with their details
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        elements = tm1.elements.get_elements(dimension_name, hierarchy_name)
        return [elem.body_as_dict for elem in elements]

@mcp.tool()
def get_leaf_elements(dimension_name: str, hierarchy_name: str) -> List[Dict]:
    """Get all leaf elements (non-consolidated) in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
    
    Returns:
        List of leaf elements with their details
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        elements = tm1.elements.get_leaf_elements(dimension_name, hierarchy_name)
        return [elem.body_as_dict for elem in elements]

@mcp.tool()
def get_leaf_element_names(dimension_name: str, hierarchy_name: str) -> List[str]:
    """Get all leaf element names (non-consolidated) in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
    
    Returns:
        List of leaf element names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.get_leaf_element_names(dimension_name, hierarchy_name)

@mcp.tool()
def get_consolidated_elements(dimension_name: str, hierarchy_name: str) -> List[Dict]:
    """Get all consolidated elements in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
    
    Returns:
        List of consolidated elements with their details
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        elements = tm1.elements.get_consolidated_elements(dimension_name, hierarchy_name)
        return [elem.body_as_dict for elem in elements]

@mcp.tool()
def get_consolidated_element_names(dimension_name: str, hierarchy_name: str) -> List[str]:
    """Get all consolidated element names in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
    
    Returns:
        List of consolidated element names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.get_consolidated_element_names(dimension_name, hierarchy_name)

@mcp.tool()
def get_elements_by_level(dimension_name: str, hierarchy_name: str, level: int) -> List[str]:
    """Get elements at a specific level in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        level: Level number to filter by
    
    Returns:
        List of element names at the specified level
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.get_elements_by_level(dimension_name, hierarchy_name, level)

@mcp.tool()
def get_element_types(dimension_name: str, hierarchy_name: str, skip_consolidations: bool = False) -> Dict:
    """Get all element types in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        skip_consolidations: Set to True to skip consolidated elements
    
    Returns:
        Dictionary mapping element names to their types
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return dict(tm1.elements.get_element_types(dimension_name, hierarchy_name, skip_consolidations))

@mcp.tool()
def get_parents(dimension_name: str, hierarchy_name: str, element_name: str) -> List[str]:
    """Get all parents of a specific element in a dimension hierarchy
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        element_name: Name of the element
    
    Returns:
        List of parent element names
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.get_parents(dimension_name, hierarchy_name, element_name)

@mcp.tool()
def get_members_under_consolidation(dimension_name: str, hierarchy_name: str, consolidation: str, 
                                   max_depth: Optional[int] = None, leaves_only: bool = False) -> List[str]:
    """Get all members under a consolidated element
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        consolidation: Name of the consolidated element
        max_depth: Maximum depth level (99 if not specified)
        leaves_only: Set to True to only return leaf elements
    
    Returns:
        List of element names under the consolidation
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.get_members_under_consolidation(
            dimension_name, hierarchy_name, consolidation, max_depth, leaves_only)

@mcp.tool()
def get_leaves_under_consolidation(dimension_name: str, hierarchy_name: str, consolidation: str,
                                  max_depth: Optional[int] = None) -> List[str]:
    """Get all leaf elements under a consolidated element
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        consolidation: Name of the consolidated element
        max_depth: Maximum depth level (99 if not specified)
    
    Returns:
        List of leaf element names under the consolidation
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.get_leaves_under_consolidation(
            dimension_name, hierarchy_name, consolidation, max_depth)

@mcp.tool()
def element_is_parent(dimension_name: str, hierarchy_name: str, parent_name: str, element_name: str) -> bool:
    """Check if an element is a direct parent of another element
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        parent_name: Name of potential parent element
        element_name: Name of element to check
    
    Returns:
        True if parent_name is a direct parent of element_name
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.element_is_parent(dimension_name, hierarchy_name, parent_name, element_name)

@mcp.tool()
def element_is_ancestor(dimension_name: str, hierarchy_name: str, ancestor_name: str, 
                       element_name: str, method: Optional[str] = None) -> bool:
    """Check if an element is an ancestor (direct or indirect parent) of another element
    
    Args:
        dimension_name: Name of the dimension
        hierarchy_name: Name of the hierarchy
        ancestor_name: Name of potential ancestor element
        element_name: Name of element to check
        method: Optional method to use for the check ('TI', 'TM1DrillDownMember', or 'Descendants')
    
    Returns:
        True if ancestor_name is an ancestor of element_name
    """
    with TM1Service(**TM1_CONFIG) as tm1:
        return tm1.elements.element_is_ancestor(
            dimension_name, hierarchy_name, ancestor_name, element_name, method)


