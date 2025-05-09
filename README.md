<img src="logo.jpg" alt="alt text" width="400"/>

# TM1 MCP Server

A Python-based project that provides a MCP server for controlling and interacting with IBM TM1 instances using any compatible LLM

## Features

- Easy access to TM1 instances through MCP
- Collection of useful TM1 tools and utilities
- Simple extension mechanism for adding custom tools

## Requirements

- Python 3.12+
- TM1 instance accessible via TM1py
- Dependencies as specified in pyproject.toml
- uv

## Installation

1. Clone this repository
2. Install dependencies

## Configuration

Modify the TM1 connection parameters in config.py as required

## Usage

Run the server:

```bash
uv run main.py
```

Run MCP inspector:

```bash
mcp dev main.py
```

Sample config for Claude Desktop (%APPDATA%/Claude/claude_desktop_config.json)
Note: Update directory arg where you save this project

```json
{
  "mcpServers": {
    "tm1": {
      "command": "uv",
      "args": [
        "--directory",
        "/ABSOLUTE/PATH/TO/TM1MCP",
        "run",
        "main.py"
      ]
    }
  }
}
```

## Extending

Add new tools by:

1. Creating new modules in the `tools/` directory
2. Decorating functions with `@mcp.tool()`
3. Importing your modules in `main.py`

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
