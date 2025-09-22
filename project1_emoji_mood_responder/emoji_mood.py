# project1_emoji_mood_responder/emoji_mood.py

import sys

# Mood dictionary mapping
mood_responses = {
    "happy": "That's great to hear! 😊",
    "sad": "Cheer up! Here's a hug 🤗",
    "angry": "Take a deep breath 😤",
    "tired": "Rest well! 😴",
    "excited": "Let’s celebrate! 🥳"
}

def get_response(user_input: str) -> str:
    """Return response based on detected mood."""
    mood = user_input.strip().lower()
    return mood_responses.get(mood, "Hmm, I’m not sure about that mood 🤔")

def main():
    print("=== Emoji Mood Responder ===")
    print("Type your mood (happy, sad, angry, tired, excited). Type 'exit' to quit.\n")

    while True:
        user_input = input("How are you feeling? ").strip().lower()
        if user_input == "exit":
            print("Goodbye! 👋")
            sys.exit()
        print(get_response(user_input))

if __name__ == "__main__":
    main()
