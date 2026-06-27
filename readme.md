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

Clone the repository:

```bash
git clone https://github.com/sunilbmnag1/langgraph.git
cd Langgraph

Create virtual environment:
python3 -m venv myenv

Activate environment:
source myenv/bin/activate

##
This project uses OpenAI API.
Create a `.env` file in the project root directory.

Add the following:
```env
OPENAI_API_KEY=your_openai_api_key_here
