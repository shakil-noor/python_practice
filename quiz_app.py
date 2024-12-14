import random
# Function to load questions from a file
def load_questions(filename):
    questions = []  # Initialize an empty list to store the questions
    try:
        # Try to open the file in read mode
        with open(filename, "r") as f:
            # Iterate through each line in the file
            for line in f:
                # Remove leading/trailing whitespace and split the line by the semicolon ';'
                parts = line.strip().split(";")
                
                # If the line contains exactly two parts (question and answer)
                if len(parts) == 2:
                    question, answer = parts  # Assign parts to question and answer variables
                    # Append a dictionary with 'question' and 'answer' to the questions list
                    questions.append({"question": question, "answer": answer})
    
    except FileNotFoundError:
        # If the file is not found, print an error message
        print(f"The file {filename} was not found")
    
    # Return the list of questions (even if empty)
    return questions

# Function to ask a question and check if the provided answer is correct
def ask_question(question, correct_answer):
    # Print the question
    print(question)
    # Get the user's input, make it lowercase and strip any extra spaces
    answer = input("Your answer: ").lower().strip()
    # Return True if the user's answer matches the correct answer, otherwise return False
    return answer == correct_answer.lower()

# Main function to run the quiz
def run_quiz():
    # Load the questions from the file 'test.txt'
    questions = load_questions("quiz_questions.txt")

    # Check if no questions were loaded (i.e., questions list is empty)
    if not questions:
        # If no questions are available, print a message and exit the function
        print("No questions to quiz!")
        return
    
    random.shuffle(questions)  # Shuffle the list of questions to make the quiz more dynamic

    score = 0  # Initialize the score counter to 0

    # Iterate through each question in the loaded questions list
    for q in questions:
        # Call the ask_question function and pass the question and answer
        if ask_question(q["question"], q["answer"]):
            # If the answer is correct, print 'correct' and increment the score
            print("correct")
            score += 1
        else:
            # If the answer is incorrect, print 'Incorrect'
            print("Incorrect")
    
    # After all questions are asked, print the final score
    print(f"\nYou got {score} out of {len(questions)} correct")

# Function to create question_list
def create_questions():
    question_list = []
    while True:
        question = input("Enter question: ")
        answer = input("Enter answer: ")
        question_list.append({"question": question, "answer": answer})

        more = input("Do you want to add another flashcard? (y/n): ").lower()
        if more != 'y':
            break
    
    # Save flashcards to a text file
    with open("quiz_questions.txt", "a") as file:  # Open the file in append mode
        for card in question_list:
            file.write(f"\n{card['question']};{card['answer']}")

    print("Questions have been saved to 'quiz_questions.txt'.")

def main():
    while True:
        # Display the menu with options for the user
        print("\n1. Play Quiz")
        print("2. Add Question")

        # Prompt user for their choice
        choice = input("Enter choice what you want to do: ")
        
        if choice == '1':
            run_quiz()
            break
        if choice == '2':
            create_questions()
            break
        else:
            print("Invalid choice! Please enter either 1 or 2.")

main()
