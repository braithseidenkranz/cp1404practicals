
def main():
    """Ask user for 5 numbers, store then, and display results"""
    numbers = []
    for i in range(5):
        number = float(input("Enter number: "))
        numbers.append(number)
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

main()