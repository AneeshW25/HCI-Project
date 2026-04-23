import os
from anthropic import Anthropic

def main():
    # Load API key securely from environment
    api_key = os.getenv("ANTHROPIC_API_KEY")

    if not api_key:
        raise EnvironmentError(
            "ANTHROPIC_API_KEY not found. Set it as an environment variable."
        )

    # Initialize Anthropic client
    client = Anthropic(api_key=api_key)

    try:
        response = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=100,
            messages=[
                {"role": "user", "content": "Explain AI in 2 lines"}
            ]
        )

        # Extract and print response safely
        for block in response.content:
            if hasattr(block, "text"):
                print(block.text)

    except Exception as e:
        print(f"Error occurred: {e}")


if __name__ == "__main__":
    main()