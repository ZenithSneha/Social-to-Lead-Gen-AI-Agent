from langgraph.graph import StateGraph, END

from agent.state import AgentState
from agent.intent import get_intent_classifier
from agent.rag import get_rag_chain
from agent.lead_flow import get_missing_lead_fields, lead_question_for
from agent.tools import mock_lead_capture


def build_graph(llm):
    graph = StateGraph(AgentState)

    intent_classifier = get_intent_classifier(llm)
    rag_chain = get_rag_chain(llm)

    # -------- Nodes --------

    def intent_node(state: AgentState):
        state.intent = intent_classifier(state.message)
        state.conversation_history.append(state.message)
        return {"intent": state.intent}

    def greeting_node(state: AgentState):
        return {
            "response": "Hi! How can I help you with AutoStream today?"
        }

    def product_node(state: AgentState):
        return {
            "response": rag_chain(state.message)
        }

    def lead_node(state: AgentState):
        missing = get_missing_lead_fields(state)

        if missing:
            return {
                "response": lead_question_for(missing[0])
            }

        mock_lead_capture(state.name, state.email, state.platform)
        return {
            "response": "Thanks! Your details have been captured. Our team will reach out shortly."
        }

    # -------- Graph wiring --------

    graph.add_node("intent", intent_node)
    graph.add_node("greeting", greeting_node)
    graph.add_node("product", product_node)
    graph.add_node("lead", lead_node)

    graph.set_entry_point("intent")

    def route(state: AgentState):
        if state.intent == "greeting":
            return "greeting"
        if state.intent == "product_query":
            return "product"
        if state.intent == "high_intent":
            return "lead"

    graph.add_conditional_edges(
        "intent",
        route,
        {
            "greeting": "greeting",
            "product": "product",
            "lead": "lead"
        }
    )

    graph.add_edge("greeting", END)
    graph.add_edge("product", END)
    graph.add_edge("lead", END)

    return graph.compile()
