"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done in the module 'tui'
        any processing should be done in the module 'process'
        any visualisation should be done in the module 'visual'
"""

import process
import tui
import visual
from exporter import DataExporter


DATA_FILE = "Disneyland_reviews.csv"


def print_title():
    title = "Disneyland Review Analyser"
    print("-" * len(title))
    print(title)
    print("-" * len(title))


def main():
    print_title()

    data = process.load_data(DATA_FILE)
    print(f"\nDataset loaded successfully. {len(data)} rows found.\n")

    running = True

    while running:
        choice = tui.main_menu()

        if choice == "A":
            sub_choice = tui.view_data_menu()

            if sub_choice == "A":
                park = tui.get_park_name()
                reviews = process.get_reviews_by_park(data, park)
                tui.display_reviews(reviews)

            elif sub_choice == "B":
                park, location = tui.get_park_and_location()
                count = process.count_reviews_by_location(data, park, location)
                print(f"\n{count} reviews from {location} for {park}\n")

            elif sub_choice == "C":
                park, year = tui.get_park_and_year()
                avg = process.average_rating_by_year(data, park, year)

                if avg == 0:
                    print("\nNo data found.\n")
                else:
                    print(f"\nAverage rating for {park} in {year}: {avg:.2f}\n")

            elif sub_choice == "D":
                results = process.average_score_by_location_all_parks(data)
                tui.display_location_averages(results)

        elif choice == "B":
            sub_choice = tui.visual_menu()

            if sub_choice == "A":
                counts = process.review_count_by_park(data)
                visual.pie_chart(counts)

            elif sub_choice == "B":
                park = tui.get_park_name()
                results = process.top_locations_by_rating(data, park)
                visual.bar_chart_locations(results, park)

            elif sub_choice == "C":
                park = tui.get_park_name()
                results = process.monthly_average_by_park(data, park)
                visual.bar_chart_months(results, park)

        elif choice == "C":
            exporter = DataExporter(data)
            format_choice = tui.export_menu()
            exporter.export(format_choice)

        elif choice == "X":
            running = False
            print("\nExiting program... Goodbye!\n")


if __name__ == "__main__":
    main()


