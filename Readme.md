# MCP (Model Context Protocol) Implementation

## Overview
This project implements the Model Context Protocol (MCP) using a server-client architecture in Python. The MCP Server handles requests related to model context management, while the MCP Client interacts with the server to send and receive data.

## Prerequisites
- Python 3.x

## Setting Up the Environment

1. **Create a Virtual Environment**
   Open a terminal and navigate to the project directory. Run the following command to create a virtual environment:
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Required Packages**
   After activating the virtual environment, install the required packages using:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Start the MCP Server**
   Open a terminal (while the virtual environment is activated) and navigate to the directory containing `mcp_server.py`. Run the following command:
   ```bash
   python mcp_server.py
   ```

2. **Start the MCP Client**
   Open another terminal window (or tab) (while the virtual environment is activated) and navigate to the directory containing `mcp_client.py`. Run the following command:
   ```bash
   python mcp_client.py
   ```

## Usage
- After starting the MCP Server, you can interact with it using the MCP Client.

## Contributing
Feel free to fork the repository and submit pull requests for any improvements or bug fixes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.