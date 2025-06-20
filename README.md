# ai-agent

A lightweight Python-based AI agent framework, designed to help you experiment with and build intelligent, task-oriented agents. 

> 🚧 This project was developed as part of the [Boot.dev](https://boot.dev) Backend Developer curriculum, serving as a practical exercise in programming, modular design, and working with AI concepts in Python.

## ✨ Features

- **Modular Agent Design:** Easily define and manage custom agents with specific behaviors.
- **Function-Based Task Execution:** Agents can call predefined functions to perform tasks, making it simple to extend functionality.
- **Configuration Support:** Customize agent behavior and function mappings with a configuration file.
- **Prompt Management:** Centralized prompt templates for consistent agent interactions.
- **Testing Framework:** Includes a testing script to validate agent logic and function calls.


## 📁 Project Structure

```
ai-agent/
├── functions/            # Custom agent function implementations
├── .gitignore            # Git ignore rules
├── README.md             # Project documentation
├── call_function.py      # Core logic for calling agent functions
├── config.py             # Configuration for agents and functions
├── main.py               # Main entry point for running agents
├── prompts.py            # Prompt templates for agent interactions
├── requirements.txt      # Python dependencies
└── tests.py              # Test cases for agent logic
```


## 🚀 Getting Started

### Prerequisites

- **Python 3.6+**
- **Basic familiarity with Python and command line**


### Installation

1. **Clone the repository:**

```bash
git clone https://github.com/jacobdanielrose/ai-agent.git
cd ai-agent
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```


### Running the Agent

Execute the main script to run the agent system:

```bash
python main.py
```


### Testing

Run the test suite to ensure agent logic is working as expected:

```bash
python tests.py
```


## 🌍 Deployment

This project is designed for local development and learning. You can extend it for deployment as a backend service or integrate it with web frameworks as needed.

## 📚 About This Project

This project was created as part of the Boot.dev Backend Developer course. It’s designed to reinforce backend fundamentals using scripting, modular design, and AI agent concepts.

## 📝 License

This project is licensed under the MIT License.

---
