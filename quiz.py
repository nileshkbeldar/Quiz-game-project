# Basic Quiz Game

# Define the quiz questions and answers
questions = [
    {
        "question": "What is the capital of France?",
        "options": ["a) Paris", "b) London", "c) Berlin", "d) Rome"],
        "answer": "a"
    },
    {
        "question": "Which is the largest planet in our solar system?",
        "options": ["a) Earth", "b) Mars", "c) Jupiter", "d) Saturn"],
        "answer": "c"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["a) O2", "b) CO2", "c) H2O", "d) N2"],
        "answer": "c"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["a) Harper Lee", "b) Mark Twain", "c) J.K. Rowling", "d) F. Scott Fitzgerald"],
        "answer": "a"
    },
    {
        "question": "Which element has the atomic number 1?",
        "options": ["a) Helium", "b) Hydrogen", "c) Oxygen", "d) Nitrogen"],
        "answer": "b"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["a) Atlantic Ocean", "b) Indian Ocean", "c) Arctic Ocean", "d) Pacific Ocean"],
        "answer": "d"
    },
    {
        "question": "In which year did World War II end?",
        "options": ["a) 1940", "b) 1942", "c) 1945", "d) 1948"],
        "answer": "c"
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": ["a) Michelangelo", "b) Leonardo da Vinci", "c) Raphael", "d) Vincent van Gogh"],
        "answer": "b"
    },
    {
        "question": "What is the square root of 64?",
        "options": ["a) 6", "b) 7", "c) 8", "d) 9"],
        "answer": "c"
    },
    {
        "question": "Which country is known as the Land of the Rising Sun?",
        "options": ["a) China", "b) Japan", "c) South Korea", "d) Thailand"],
        "answer": "b"
    }
]

# Function to display the question and get user's answer
def ask_question(question_dict):
    print(question_dict["question"])
    for option in question_dict["options"]:
        print(option)
    answer = input("Enter your answer (a/b/c/d): ").lower()
    return answer

# Function to check the answer and provide feedback
def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        print("Correct!\n")
        return True
    else:
        print(f"Incorrect! The correct answer was {correct_answer}.\n")
        return False

# Main function to run the quiz
def run_quiz():
    print("Welcome to the Basic Quiz Game!\n")
    score = 0

    for question in questions:
        user_answer = ask_question(question)
        if check_answer(user_answer, question["answer"]):
            score += 1

    print(f"Your final score is {score}/{len(questions)}.")

if __name__ == "__main__":
    run_quiz()
