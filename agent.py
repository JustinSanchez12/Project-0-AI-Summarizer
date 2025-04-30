from langchain.agents import initialize_agent, AgentType
from langchain_community.chat_models import ChatOllama
from tools.tools import make_summarize_paragraph_tool, highlight_text_tool, scrape_and_summarize_tool

# Set up Ollama with Gemma 
llm = ChatOllama(
    model="gemma3:4b",
    temperature=0.7,
)

summarize_paragraph = make_summarize_paragraph_tool(llm)
highlight_text = highlight_text_tool(llm)
scrape_text = scrape_and_summarize_tool(llm)

# Add tools to the agent
tools = [summarize_paragraph, highlight_text, scrape_text]

# Initialize the agent with tool-calling enabled
agent_executor = initialize_agent(
    tools=tools,
    llm=llm,
    agent=AgentType.OPENAI_FUNCTIONS,  # Tool-calling enabled
    verbose=True
)

# Simple loop to interact with the agent
print("Type 'exit' to quit.")
while True:
    user_input = input("\nInsert Prompt: ")
    if user_input.lower() in ['exit', 'quit']:
        break
    response = agent_executor.invoke(user_input)
    print("\nGemma:", response)