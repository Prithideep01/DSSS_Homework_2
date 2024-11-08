import random

def generate_random_integer(min_value, max_value):
    """
    Generate a random integer within a specified range.
    
    Args:
        min_value (int): The lower bound of the random integer.
        max_value (int): The upper bound of the random integer.

    Returns:
        int: A random integer between min_value and max_value (both inclusive).
    """
    return random.randint(min_value, max_value)

def get_random_operation():
    """
    Select a random mathematical operation.

    Returns:
        str: A random operation symbol from '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])

def create_math_problem(number1, number2, operation):
    """
    Formulate a math problem and compute its answer based on the given numbers and operation.

    Args:
        number1 (int): The first number in the math problem.
        number2 (int): The second number in the math problem.
        operation (str): The mathematical operation to apply ('+', '-', '*').

    Returns:
        tuple: A tuple containing the formatted math problem as a string and its answer as an integer.
    """
    if operation == '+':
        computer_answer = number1 + number2
    elif operation == '-':
        computer_answer = number1 - number2
    else:  # '*' operation
        computer_answer = number1 * number2

    problem_text = f"{number1} {operation} {number2}"
    return problem_text, computer_answer

def math_quiz():
    """
    Run the math quiz game where the user answers randomly generated math problems.
    
    The game gives feedback on each answer and displays the final score.
    """
    score = 0
    total_questions = 3  # Set a fixed number of questions for the quiz

    print("Welcome to the Math Quiz Game!")
    print("Answer the math problems correctly to earn points.")

    for _ in range(total_questions):
        # Generate numbers and a random operation for the math problem
        number1 = generate_random_integer(1, 10)
        number2 = generate_random_integer(1, 5)  # Only goes up to 5
        operation = get_random_operation()

        # Formulate the math problem and calculate the correct answer
        problem_text, correct_answer = create_math_problem(number1, number2, operation)
        print(f"\nQuestion: {problem_text}")

        # Get and validate user input
        try:
            user_input = input("Your answer: ")
            user_answer = int(user_input)
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue  # Skip to the next question if input is invalid

        # Check the user's answer
        if user_answer == correct_answer:
            print("Correct! You earned a point.")
            score += 1
        else:
            print(f"Wrong answer. The correct answer was {correct_answer}.")

    # Display the final score
    print(f"\nGame over! Your score is: {score}/{total_questions}")

if _name_ == "_main_":
    math_quiz()