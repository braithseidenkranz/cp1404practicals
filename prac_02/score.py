"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    result = get_score_result(score)
    print(result)

    random_score = random.randint(0, 100)
    print(f"Random score is {random_score}")
    random_score_result = get_score_result(random_score)
    print(f"{random_score_result}")


def get_score_result(score):
    """Return the result based on the score"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()