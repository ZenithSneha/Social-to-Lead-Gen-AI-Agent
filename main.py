from agent.graph import build_graph
from agent.state import AgentState
from agent.mock_llm import MockLLM


def main():
    llm = MockLLM()
    graph = build_graph(llm)
    state = AgentState()

    print("AutoStream Agent is running. Type 'exit' to stop.\n")

    while True:
        user_input = input("User: ")

        if user_input.lower() == "exit":
            print("Exiting AutoStream Agent.")
            break

        # Put user input into state
        state.message = user_input

        # LangGraph returns a DICT of updates
        updates = graph.invoke(state)

        # Merge updates back into state safely
        for key, value in updates.items():
            setattr(state, key, value)

        # Print agent response
        if state.response:
            print("Agent:", state.response)


if __name__ == "__main__":
    main()
