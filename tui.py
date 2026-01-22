"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""


def main_menu():
    print("Please enter the letter which corresponds with your desired menu choice:")
    print("[A] View Data")
    print("[B] Visualise Data")
    print("[C] Export Data")
    print("[X] Exit")

    choice = input("\n").upper()

    if choice in ["A", "B", "C", "X"]:
        print(f"You have chosen option {choice}\n")
        return choice

    print("Invalid option\n")
    return main_menu()


def view_data_menu():
    print("\nPlease enter one of the following options:")
    print("[A] View all reviews for a park")
    print("[B] Count reviews by location")
    print("[C] Average rating by year")
    print("[D] Average score per park by location")

    return input("\n").upper()


def visual_menu():
    print("\nVisualisation Menu:")
    print("[A] Most reviewed parks (Pie Chart)")
    print("[B] Top 10 locations by rating (Bar Chart)")
    print("[C] Monthly average rating (Bar Chart)")

    return input("\n").upper()


def export_menu():
    print("\nExport Format:")
    print("[TXT]")
    print("[CSV]")
    print("[JSON]")

    return input("\n").upper()


def get_park_name():
    return input("\nEnter park name: ").strip()


def get_park_and_location():
    park = input("\nEnter park name: ").strip()
    location = input("Enter reviewer location: ").strip()
    return park, location


def get_park_and_year():
    park = input("\nEnter park name: ").strip()
    year = input("Enter year (YYYY): ").strip()
    return park, year


def display_reviews(reviews):
    if not reviews:
        print("\nNo reviews found.\n")
        return

    for r in reviews:
        print(f"{r['Year_Month']} | {r['Reviewer_Location']} | Rating: {r['Rating']}")
    print()


def display_location_averages(results):
    for park, locations in results.items():
        print(f"\n{park}")
        for loc, avg in locations.items():
            print(f"  {loc}: {avg:.2f}")

