from browser import document, bind
# Note: If you could avoid unnecessary import, your script will save several seconds loading time
# For example, use `"message".title()` instead of `import string; string.capwords("message")`

import datetime
from collections import Counter

from dateutil.easter import easter  # Came from python-dateutil package
from charts.css import bar, column, line  # Came from charts.css.py package


def easter_stat(starting_year):
    easters = list(easter(year) for year in range(starting_year, starting_year + 100))

    months = Counter(e.month for e in easters)
    easters_per_month = sorted(months.items())
    document["easters_per_month"].html = bar(
        easters_per_month,
        headers_in_first_column=True,
        heading="How many Easters happen per month during the sampling period",
        )

    dates = Counter("{}-{:>2}".format(e.month, e.day) for e in easters)
    easters_per_date = sorted(dates.items())
    document["easters_per_date"].html = column(
        easters_per_date,
        headers_in_first_column=True,
        heading="How many Easters happen per date during the sampling period",
        )

    year_by_year = [(e, (e - datetime.date(e.year, 1, 1)).days) for e in easters]
    document["year_by_year"].html = line(
        year_by_year,
        heading="""How Easter day swings back and forth, year after year.
(Y-axis is the number of days between January 1st to Easter data of that year)""",
        headers_in_first_column=True,
        hide_label=lambda row_number, header: bool(row_number % 10),  # Hide most labels
        hide_data=True,  # Otherwise it would be messy
        tooltip_builder="{label}".format,
        )

@bind("#trigger", "click")
def trigger(event):
    easter_stat(int(document["year_starts_at"].value))

