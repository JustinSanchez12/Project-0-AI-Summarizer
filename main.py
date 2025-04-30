from agent import agent_executor

def main():
    print("Welcome to the LLM Web Summarizer Agent.")
    print("Type 'exit' to quit.")
    while True:
        user_input = input("\nInsert Prompt (or URL): ")
        if user_input.lower() in ['exit', 'quit']:
            break
        try:
            response = agent_executor.invoke(user_input)
            print("\nGemma:", response)
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()
