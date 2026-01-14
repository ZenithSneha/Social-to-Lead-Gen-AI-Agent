def get_rag_chain(_llm=None):
    def rag_response(question: str) -> str:
        q = question.lower()

        if "basic" in q:
            return (
                "The Basic plan costs $29 per month and includes "
                "10 videos per month with 720p resolution."
            )

        if "pro" in q:
            return (
                "The Pro plan costs $79 per month and includes "
                "unlimited videos, 4K resolution, and AI captions."
            )

        if "refund" in q:
            return "AutoStream does not offer refunds after 7 days."

        return "I don't have that information at the moment."

    return rag_response
