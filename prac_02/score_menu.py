"""Score program with menu options"""

MENU = "G - Get score\nP - Print result\nS - Show stars\nQ - Quit"

def main():
    score = get_valid_score()

    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = determine_result(score)
            print(f"A score of {score} is considered {result}")
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you, Goodbye :)")


def get_valid_score():
    """Get valid score from user between 0 and 100"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Score must be between 0 and 100")
        score = float(input("Enter score: "))
    return int(score)

def determine_result(score):
    """Return the result based on the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

def show_stars(score):
    """Print line of stars based on the score"""
    print("*" * score)

main()