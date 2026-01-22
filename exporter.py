import json
import csv
from collections import defaultdict


class DataExporter:
    def __init__(self, data):
        self.data = data
        self.summary = self._generate_summary()

    def _generate_summary(self):
        parks = defaultdict(lambda: {
            "reviews": 0,
            "positive": 0,
            "ratings": [],
            "countries": set()
        })

        for r in self.data:
            park = r["Branch"]
            rating = r["Rating"]

            parks[park]["reviews"] += 1
            parks[park]["ratings"].append(rating)
            parks[park]["countries"].add(r["Reviewer_Location"])

            if rating >= 4:
                parks[park]["positive"] += 1

        final = {}
        for park, stats in parks.items():
            final[park] = {
                "Number of Reviews": stats["reviews"],
                "Positive Reviews": stats["positive"],
                "Average Score": sum(stats["ratings"]) / len(stats["ratings"]),
                "Countries": len(stats["countries"])
            }

        return final

    def export(self, format_type):
        if format_type == "TXT":
            self._export_txt()
        elif format_type == "CSV":
            self._export_csv()
        elif format_type == "JSON":
            self._export_json()
        else:
            print("Invalid format")

    def _export_txt(self):
        with open("export.txt", "w") as file:
            for park, data in self.summary.items():
                file.write(f"{park}\n")
                for k, v in data.items():
                    file.write(f"  {k}: {v}\n")
        print("\nExported to export.txt\n")

    def _export_csv(self):
        with open("export.csv", "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Park", "Reviews", "Positive", "Average", "Countries"])

            for park, data in self.summary.items():
                writer.writerow([
                    park,
                    data["Number of Reviews"],
                    data["Positive Reviews"],
                    round(data["Average Score"], 2),
                    data["Countries"]
                ])

        print("\nExported to export.csv\n")

    def _export_json(self):
        with open("export.json", "w") as file:
            json.dump(self.summary, file, indent=4)

        print("\nExported to export.json\n")