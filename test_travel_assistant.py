
from travel_assistant import answer_travel_question


def main():
    print("=" * 45)
    print("      WANDERWISE AI TRAVEL ASSISTANT")
    print("=" * 45)
    print("Ask me anything about travel!")
    print("Type 'exit' to stop.\n")

    chat_history = []

    while True:
        question = input("You: ").strip()

        if question.lower() in ("exit", "quit"):
            print("WanderWise: Happy travels!")
            break

        if not question:
            print("WanderWise: Please enter a question.")
            continue

        answer = answer_travel_question(
            question,
            chat_history
        )

        print("\nWanderWise:", answer, "\n")

        # Save the conversation for follow-up questions.
        chat_history.append({
            "role": "user",
            "content": question
        })

        chat_history.append({
            "role": "assistant",
            "content": answer
        })


if __name__ == "__main__":
    main()
