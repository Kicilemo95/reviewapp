"""
This module is responsible for visualising the data using Matplotlib.
Any visualisations should be generated via functions in this module.
"""



def pie_chart(data):
    plt.figure()
    plt.pie(data.values(), labels=data.keys(), autopct="%1.1f%%")
    plt.title("Number of Reviews per Park")
    plt.show()


def bar_chart_locations(data, park):
    plt.figure()
    plt.bar(data.keys(), data.values())
    plt.xticks(rotation=45, ha="right")
    plt.title(f"Top 10 Locations by Rating - {park}")
    plt.ylabel("Average Rating")
    plt.tight_layout()
    plt.show()


def bar_chart_months(data, park):
    plt.figure()
    plt.bar(data.keys(), data.values())
    plt.title(f"Monthly Average Ratings - {park}")
    plt.xlabel("Month")
    plt.ylabel("Average Rating")
    plt.show()

