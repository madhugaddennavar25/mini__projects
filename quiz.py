import random
from colorama import Fore, Style, init

# Initialize colorama for Windows/VS Code compatibility
init(autoreset=True)

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

def print_colored(text, color):
    colors = {
        "green": Fore.GREEN,
        "red": Fore.RED,
        "yellow": Fore.YELLOW,
        "cyan": Fore.CYAN
    }
    print(colors.get(color, "") + text + Style.RESET_ALL)

def ask_question(index, question, options):
    print(f'Question {index}: {question}')
    for option in options:
        print(option)
    return input('Your answer: ').upper().strip()

def run_quiz(quiz):
    random.shuffle(quiz)
    score = 0

    for index, item in enumerate(quiz, 1):
        answer = ask_question(index, item[QUESTION], item[OPTIONS])

        if answer == item[ANSWER]:
            print_colored('Correct!', 'green')
            score += 1
        else:
            print_colored(f'Wrong! The correct answer is {item[ANSWER]}', 'red')
        print()

    print(f'Quiz over! Your final score is {score} out of {len(quiz)}')
    percentage = (score / len(quiz)) * 100
    print_colored(f'Your percentage: {percentage:.2f}%', 'cyan')

    if percentage == 100:
        print_colored("Excellent! Perfect score!", "green")
    elif percentage >= 60:
        print_colored("Good job! You passed.", "yellow")
    else:
        print_colored("Better luck next time.", "red")

def main():
    quiz = [
        {
            QUESTION: ' Which continent has land in all four hemispheres?',
            OPTIONS: ['A. asia', 'B. north america', 'C. africa', 'D. europe'],
            ANSWER: 'C'
        },
        {
            QUESTION: 'Which planet is known as the red planet?',
            OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
            ANSWER: 'B'
        },
        {
            QUESTION: 'What is the largest ocean on Earth?',
            OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
            ANSWER: 'D'
        }
    ]
    run_quiz(quiz)

if __name__ == '__main__':
    main()


