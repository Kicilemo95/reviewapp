"""
This module is responsible for processing the data.  It will largely contain functions that will recieve the overall dataset and 
perfrom necessary processes in order to provide the desired result in the desired format.
It is likely that most sections will require functions to be placed in this module.
"""
import csv
from collections import defaultdict


def load_data(filename):
    data = []
    with open(filename, newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["Rating"] = int(row["Rating"])
            data.append(row)
    return data


def get_reviews_by_park(data, park):
    return [r for r in data if r["Branch"].lower() == park.lower()]


def count_reviews_by_location(data, park, location):
    return sum(
        1 for r in data
        if r["Branch"].lower() == park.lower()
        and r["Reviewer_Location"].lower() == location.lower()
    )


def average_rating_by_year(data, park, year):
    ratings = [
        r["Rating"] for r in data
        if r["Branch"].lower() == park.lower()
        and r["Year_Month"].startswith(year)
    ]

    return sum(ratings) / len(ratings) if ratings else 0


def review_count_by_park(data):
    counts = defaultdict(int)
    for r in data:
        counts[r["Branch"]] += 1
    return dict(counts)


def top_locations_by_rating(data, park):
    totals = defaultdict(list)

    for r in data:
        if r["Branch"].lower() == park.lower():
            totals[r["Reviewer_Location"]].append(r["Rating"])

    averages = {
        loc: sum(scores) / len(scores)
        for loc, scores in totals.items()
    }

    return dict(sorted(averages.items(), key=lambda x: x[1], reverse=True)[:10])


def monthly_average_by_park(data, park):
    months = defaultdict(list)

    for r in data:
        if r["Branch"].lower() == park.lower():
            date = r["Year_Month"]

            if "-" in date:
                parts = date.split("-")
                if len(parts) == 2:
                    month = parts[1]
                    months[month].append(r["Rating"])

    return {
        m: sum(scores) / len(scores)
        for m, scores in sorted(months.items())
    }


def average_score_by_location_all_parks(data):
    results = defaultdict(lambda: defaultdict(list))

    for r in data:
        results[r["Branch"]][r["Reviewer_Location"]].append(r["Rating"])

    final = {}
    for park, locations in results.items():
        final[park] = {
            loc: sum(scores) / len(scores)
            for loc, scores in locations.items()
        }

    return final

