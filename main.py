def get_output(mood, productivity, stress):
    mood = mood.lower()
    productivity = productivity.lower()
    stress = stress.lower()

    if mood == "good" and productivity == "high" and stress == "low":
        return "Growth Day"

    elif mood == "good" and productivity == "low":
        return "Improvement Day"

    elif mood == "neutral" and productivity == "medium":
        return "Maintenance Day"

    elif mood == "bad" and stress == "high":
        return "Recovery Day"

    elif mood == "bad" and productivity == "low":
        return "Warning Day"

    else:
        return "Undefined Case"


def ai_suggestion(category):
    suggestions = {
        "Growth Day": "Keep up the great habits.",
        "Improvement Day": "Plan better for higher productivity.",
        "Maintenance Day": "Stay consistent.",
        "Recovery Day": "Focus on rest.",
        "Warning Day": "Start with small tasks."
    }
    return suggestions.get(category, "")


if __name__ == "__main__":
    mood = input("Mood: ")
    productivity = input("Productivity: ")
    stress = input("Stress: ")

    result = get_output(mood, productivity, stress)
    print("\nCategory:", result)
    print("Suggestion:", ai_suggestion(result))