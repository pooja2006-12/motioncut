# project2_emotion_detector/emotion_detector.py

import re
from collections import Counter

# Simple emotion keyword dictionary
emotion_keywords = {
    "happy": "Joy 😊",
    "joy": "Joy 😊",
    "glad": "Joy 😊",
    "excited": "Excitement 🥳",
    "cry": "Sadness 😢",
    "sad": "Sadness 😔",
    "angry": "Anger 😡",
    "mad": "Anger 😠",
    "fear": "Fear 😨",
    "scared": "Fear 😱",
    "tired": "Tiredness 😴"
}

def detect_emotion(sentence: str) -> str:
    """Detect dominant emotion from sentence."""
    words = re.findall(r"\w+", sentence.lower())
    counts = Counter()

    for word in words:
        if word in emotion_keywords:
            counts[emotion_keywords[word]] += 1

    if not counts:
        return "No strong emotion detected 🤔"
    return f"Detected Emotion: {counts.most_common(1)[0][0]}"

def main():
    print("=== Emotion Detector ===")
    print("Type a sentence about how you feel. Type 'exit' to quit.\n")

    while True:
        sentence = input("Enter your sentence: ").strip()
        if sentence.lower() == "exit":
            print("Goodbye! 👋")
            break
        print(detect_emotion(sentence))

if __name__ == "__main__":
    main()
