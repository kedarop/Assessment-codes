# Knowledge base for troubleshooting computer issues
knowledge_base = {
    "Is the computer powering on?": {
        "Yes": {
            "Is there a beeping sound?": {
                "Yes": "Check the RAM and CPU.",
                "No": {
                    "Is the display showing any output?": {
                        "Yes": "Check the display connections and settings.",
                        "No": "Check the power supply and motherboard."
                    }
                }
            }
        },
        "No": "Check the power supply and cables."
    }
}

def troubleshoot_computer(issue_tree):
    """Recursively asks questions based on the decision tree until a solution is reached."""
    current_question = issue_tree

    while isinstance(current_question, dict):
        # Get the first question from the current dictionary
        question = next(iter(current_question))
        print(question)  # Display the question
        
        
        user_response = input("Enter 'Yes' or 'No': ").strip().capitalize()
        
        
        if user_response in current_question[question]:
            current_question = current_question[question][user_response]
        else:
            print("Please respond with 'Yes' or 'No'.")
            return

   
    print(f"Suggested action: {current_question}")


if __name__ == "__main__":
    print("Welcome to the Computer Troubleshooting Assistant!")
    troubleshoot_computer(knowledge_base)
