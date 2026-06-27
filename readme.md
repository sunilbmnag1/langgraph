# LangGraph Practice Projects

This repository contains practice workflows built using LangGraph.

The goal of this project is to learn how to build stateful AI workflows using LangGraph, including:
- Sequential workflows
- Conditional edges
- State management
- Tool calling
- Multi-step agent execution

## Tech Stack

- Python 3.13
- LangGraph
- LangChain
- OpenAI API
- Jupyter Notebook (.ipynb)

## Setup Instructions

```bash
git clone https://github.com/sunilbmnag1/langgraph.git
cd langgraph

Create virtual environment:
```bash
python3 -m venv myenv

Activate environment:
```bash
source myenv/bin/activate

Environment Variables
This project uses the OpenAI API.
Create a .env file in the root directory of the project.
Add the following:

OPENAI_API_KEY=<your_openai_api_key_here>
