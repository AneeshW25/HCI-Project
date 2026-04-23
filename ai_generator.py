import random

def generate_explanation(title, content):
    # Sentence templates (makes output look AI-like)
    openings = [
        f"This slide focuses on {title}.",
        f"Here, we are discussing {title}.",
        f"This part of the presentation explains {title}."
    ]

    connectors = [
        "In particular,",
        "More specifically,",
        "The key idea is that",
        "It highlights that"
    ]

    conclusions = [
        "Overall, this helps in understanding the concept clearly.",
        "This gives a better insight into the topic.",
        "This is important for building a strong understanding.",
        "This plays a crucial role in the overall system."
    ]

    explanation = random.choice(openings) + "\n\n"

    if content:
        explanation += random.choice(connectors) + " " + content + ".\n\n"

    explanation += random.choice(conclusions)

    return explanation