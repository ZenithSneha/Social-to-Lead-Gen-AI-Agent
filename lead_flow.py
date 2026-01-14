def get_missing_lead_fields(state):
    missing = []

    if not state.name:
        missing.append("name")
    if not state.email:
        missing.append("email")
    if not state.platform:
        missing.append("platform")

    return missing


def lead_question_for(field):
    questions = {
        "name": "May I have your name?",
        "email": "Could you please share your email address?",
        "platform": "Which platform do you create content on? (YouTube, Instagram, etc.)"
    }
    return questions[field]
