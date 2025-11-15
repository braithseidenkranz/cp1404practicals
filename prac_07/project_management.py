
from datetime import datetime, date
from project import Project

MENU = "(L)oad projects\n(S)ave projects\n(D)isplay projects\n(F)ilter projects by date\n(A)dd new project\n(U)pdate project\n(Q)uit"
DEFAULT_FILENAME = "projects.txt"
DATE_FMT = "%d/%m/%Y"

def main():
    print("Welcome to Pythonic Project Management")
    projects = load_projects(DEFAULT_FILENAME)
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    print(MENU)
    choice = input(">>>").upper()
    while choice != "Q":
        if choice == "L":
            filename = input("Filename to load: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "S":
            filename = input("Filename to save: ").strip()
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "D":
            display_projects(projects)
        elif choice == "F":
            filter_projects_by_date(projects)
        elif choice == "A":
            add_new_project(projects)
        elif choice == "U":
            update_project(projects)
        else:
            print("Invalid menu option")
        print(MENU)
        choice = input(">>>").upper()
    answer = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip()
    if answer and answer[0].lower() == "y":
        save_projects(DEFAULT_FILENAME, projects)
        print(f"Saved {len(projects)} projects to {DEFAULT_FILENAME}")

    print("Thank you for using custom-built project management software.")
def load_projects(filename):
    projects = []
    with open(filename, 'r') as in_file:
        in_file.readline() #ignore the header
        for line in in_file:
            parts = line.strip().split("\t")
            start_dt = datetime.strptime(parts[1], DATE_FMT).date()
            project = Project(parts[0], start_dt, int(parts[2]), float(parts[3]), int(parts[4]))
            projects.append(project)
    return projects

def save_projects(filename, projects):
    with open(filename, 'w') as out_file:
        print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
        for p in projects:
            print(f"{p.name}\t{p.start_date.strftime(DATE_FMT)}\t{p.priority}\t{p.estimate}\t{p.completion}", file=out_file)

def display_projects(projects):
    incomplete = [project for project in projects if not project.is_complete()]
    complete = [project for project in projects if project.is_complete()]

    incomplete.sort()
    complete.sort()

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in complete:
        print(f"  {project}")

def get_start_date(project):
    return project.start_date

def add_new_project(projects):
    print("Let's add a new project")
    name = input("Name: ").strip()
    start_str = input("Start date (dd/mm/yyyy): ").strip()
    priority = int(input("Priority: ").strip())
    estimate = float(input("Cost estimate: $").strip())
    completion = int(input("Percent complete: ").strip())

    start_dt = datetime.strptime(start_str, DATE_FMT).date()
    projects.append(Project(name, start_dt, priority, estimate, completion))

def filter_projects_by_date(projects):
    date_str = input("Show projects that start after date (dd/mm/yyyy): ").strip()
    try:
        cutoff = datetime.strptime(date_str, DATE_FMT).date()
    except ValueError:
        print("Invalid date format")
        return

    filtered = [project for project in projects if project.start_date > cutoff]
    filtered.sort(key=get_start_date)

    for project in filtered:
        print(project)

def update_project(projects):
    """Allow the user to choose a project and update its completion and/or priority."""
    print("Projects:")
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    try:
        project_index = int(input("Project choice: ").strip())
        project_to_update = projects[project_index]
    except (ValueError, IndexError):
        print("Invalid project selection.")
        return

    print(f"Selected: {project_to_update}")

    new_percentage = input("New Percentage: ").strip()
    new_priority = input("New Priority: ").strip()

    # Only update if the user entered something
    if new_percentage:
        try:
            project_to_update.completion = int(new_percentage)
        except ValueError:
            print("Invalid percentage — value not changed.")

    if new_priority:
        try:
            project_to_update.priority = int(new_priority)
        except ValueError:
            print("Invalid priority — value not changed.")

    print("Project updated successfully.")

main()