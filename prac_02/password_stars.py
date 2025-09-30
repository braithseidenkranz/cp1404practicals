
MIN_LENGTH = 5

def main():
    password = get_password()
    print_stars(password)

def get_password():
    password = input(f"Enter password (at least {MIN_LENGTH} characters): ")
    while len(password) < 4:
        password = input(f"Enter password (at least {MIN_LENGTH} characters): ")
        print(f"Password must be at least {MIN_LENGTH} characters")
    return password

def print_stars(password):
    print("*" * len(password))

main()