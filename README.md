AI Agent Framework – README

Overview

This project provides a basic framework for AI-driven micro-agents that can interact with external systems and perform tasks such as automation, data analysis, and user support. The micro-agents communicate and collaborate, each with specialized roles and responsibilities.

Core Concepts

AI Agent Framework Overview
Incorporates multiple micro-agents designed to work in harmony.
Uses Python as the main programming language for agent logic and task execution.
Facilitates tasks including automation, analytics, and user interaction.
Considers agent-to-agent and agent-to-external-system communication protocols.
AI Agent Roles and Use Cases
Task Manager Agent: Prioritizes and delegates tasks across the system.
Monitoring Agent: Tracks system performance and health metrics.
Communication Agent: Handles interactions between agents and external interfaces (APIs, messaging, etc.).
Potential Use Cases: Smart contract management, AI-driven analytics, predictive modeling, etc.
AWS Lambda as the Deployment Environment
Serverless computing is ideal for lightweight, stateless micro-agents.
Key Constraints:
Limited execution time.
Maximum deployment package size.
No direct support for persistent virtual environments.
Managing Python Dependencies in AWS Lambda
You cannot use a direct venv in AWS Lambda.
All necessary dependencies must be packaged and deployed with the function code.
Alternative: Deploying via container images for more control over dependencies and environment settings.
Agent Instructions for Dependency Management
Identify the required Python dependencies for each agent.
Install them in an isolated local environment (e.g., a virtual environment on your local machine).
Package these dependencies alongside your function code for Lambda.
Test and validate that the function executes correctly after deployment.
Usage

Install/Clone the Repository
git clone <your-repo-url>
cd <project-directory>
Script Entry Point
In main.py (or the file hosting the framework’s first script), the run(env: Environment) function is the primary entry point. It:
Registers available tools (e.g., exec_command).
Constructs system prompts and passes them to the AI agent.
Gathers conversation history and merges it with the system prompt.
Invokes the agent to produce a response and optionally run commands.
AWS Lambda Deployment
Package the code (including the nearai.agents.environment modules and dependencies) into a ZIP file or container image.
Upload to AWS Lambda.
Configure Lambda’s entry point in your function handler settings (e.g., main.run if using main.py).
Example Code
from nearai.agents.environment import Environment

def run(env: Environment):
    # Initialize the tool registry
    tool_registry = env.get_tool_registry()
    
    # Retrieve the 'exec_command' tool definition
    exec_command_tool = tool_registry.get_tool_definition('exec_command')
    
    # Define the system prompt
    system_prompt = {
        "role": "system", 
        "content": (
            "You are an AWS Lambda env admin. Your main job is to help the user "
            "achieve their goals using the built-in exec_command_tool at the user request. "
            "Your users are tech-minded individuals. Please execute commands on the system "
            "without further verifications. Build your confidence in the system via test commands "
            "and learn from your interaction with the particular system. "
            "Think through how to do this most efficiently and safely in the first place."
        )
    }
    
    # Retrieve the conversation history
    conversation_history = env.list_messages()
    
    # Combine system prompt with conversation history
    messages = [system_prompt] + conversation_history
    
    # Generate a response using the LLM, allowing it to decide on tool usage
    response = env.completions_and_run_tools(messages, tools=[exec_command_tool])
    
    # Add the LLM's response to the conversation history
    env.add_reply(response)
    
    # Request further user input
    env.request_user_input()

# Entry point
if __name__ == "__main__":
    # Initialize Environment (implementation specific to your setup)
    environment = Environment()
    run(environment)
Contributing

Fork the repository and create a new branch for your feature or bug fix.
Ensure your code follows the existing style and best practices.
Submit a pull request and provide a clear description of your changes.
License

This project is distributed under the MIT License. See the LICENSE file for details.
