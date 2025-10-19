"""Estimate: 20min, Actual: 26min"""

def main():
    email_to_name = {}
    email =  input("Email: ")
    while email != "":
        name = extract_name(email)
        is_name_correct = input(f"Is your name {name}? (Y/N)").strip().lower()

        if is_name_correct not in ('', 'y', 'yes'):
            name = input("Name: ").title()

        email_to_name[email]  = name
        email = input("Email: ")

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extracts the name from the email"""
    start_of_email = email.split('@')[0]
    parts = start_of_email.split('.')
    name = " ".join(parts).title()
    return name


main()