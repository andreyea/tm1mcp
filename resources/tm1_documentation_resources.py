from server import mcp
import chromadb

client = chromadb.PersistentClient(path="./data/ti_documentation")
collection = client.get_or_create_collection(name="tm1")

@mcp.resource("docs://ti/search/{query_text}")
def get_documentation(query_text:str) -> str:
    """Search TM1 turbo integrator (TI) documentation 
    
    Args:
        query_text: Natural language query to search for in the documentation
        
    Returns:
        The most relevant documentation text based on the query
    """
    result = collection.query(query_texts=[query_text],include=["documents"], n_results=1)    
    return str(result)