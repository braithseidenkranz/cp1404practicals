"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subject_records = load_subject_records(FILENAME)
    print(subject_records)
    display_subject_details(subject_records)


def load_subject_records(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    input_file = open(filename)
    subject_records = []
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        subject_records.append(parts)
    input_file.close()
    return subject_records

def display_subject_details(subject_details):
    """Display formatted subject details from the nested list"""
    print("\nSubject details:")
    for record in subject_details:
        subject_code = record[0]
        lecturer = record[1]
        number_of_students = record[2]
        print(f"{subject_code} is taught by {lecturer} and has {number_of_students} students.\n")
main()