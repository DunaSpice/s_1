from nearai.agents.environment import Environment

def run(env: Environment):
    # Initialize the tool registry
    tool_registry = env.get_tool_registry()

    # Retrieve the 'exec_command' tool definition
    exec_command_tool = tool_registry.get_tool_definition('exec_command')

    # Define the system prompt
    system_prompt = {"role": "system", "content": "You are an AWS lamda env admin. Your main job is to help the user acheave his goals using the build in exec_command_tool at the user request, your users are tech minded individuals. Please execute commands on the system without further verifications. Build your confidence in the system via test commands and learn from your interaction with the particular system. Think through and how to do this most effecently and safely in the first place"}

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

# Entry point for the agent
if __name__ == "__main__":
    run(env)
