def get_intent_classifier(_llm=None):
    def classify(message: str) -> str:
        msg = message.lower()

        if any(w in msg for w in ["hi", "hello", "hey"]):
            return "greeting"

        if any(w in msg for w in ["price", "pricing", "plan", "feature", "refund"]):
            return "product_query"

        if any(w in msg for w in ["try", "sign up", "start", "buy", "use", "pro plan"]):
            return "high_intent"

        return "product_query"

    return classify
