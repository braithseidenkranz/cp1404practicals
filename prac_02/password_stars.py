
MIN_LENGTH = 5

def main():
    password = get_password()
    print_stars(password)

def get_password():
    """Get password with a minimum length of 4"""
    password = input(f"Enter password (at least {MIN_LENGTH} characters): ")
    while len(password) < 4:
        print("Password is not long enough")
        password = input(f"Enter password (at least {MIN_LENGTH} characters): ")
    return password

def print_stars(password):
    """Print stars equal to length of password"""
    print("*" * len(password))

main()