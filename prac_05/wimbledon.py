"""Estimate: 35min, Actual:40min """

FILENAME = "wimbledon.csv"

def main():

    wimbledon_data = read_file_records(FILENAME)
    champion_to_wins = count_champions_wins(wimbledon_data)
    countries = find_winning_countries(wimbledon_data)

    print("Wimbledon Champions: ")
    max_name_length = max(len(name) for name in champion_to_wins)
    for champion, wins in champion_to_wins.items():
        print(f"{champion:{max_name_length}} {wins}")

    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def read_file_records(filename):
    """Read the CSV file and return a list of lists"""
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        in_file.readline() #remove header
        wimbledon_data = [line.strip().split(",") for line in in_file]
    return wimbledon_data

def count_champions_wins(wimbledon_data):
    """Count how many wins each champion has"""
    champion_to_wins = {}
    for record in wimbledon_data:
        champion = record[2]
        try:
            champion_to_wins[champion] += 1
        except KeyError:
            champion_to_wins[champion] = 1
    return champion_to_wins

def find_winning_countries(wimbledon_data):
    """Create a set of the countries that have won"""
    countries = {record[1] for record in wimbledon_data}
    return countries


main()