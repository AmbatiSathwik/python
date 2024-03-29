import csv
import sys

import psycopg2 as pg


def insert_csv_file(fname):

    dbconn = pg.connect(database="covidcases")
    cursor = dbconn.cursor()
    cursor.execute("DELETE FROM covid_data")
    f = open(fname)
    reader = csv.reader(f)
    for (
        state,
        total_cases,
        increase_today,
        active_cases,
        recovered,
        recovered_today,
        deaths,
        death_today,
    ) in reader:
        cursor.execute(
            "INSERT INTO covid_data(state,total_cases , increase_today , active_cases , recovered , recovered_today , deaths , death_today) VALUES (%s,%s,%s,%s, %s,%s ,%s,%s)",
            (
                state,
                total_cases,
                increase_today,
                active_cases,
                recovered,
                recovered_today,
                deaths,
                death_today,
            ),
        )

    dbconn.commit()


def main():
    fname = "covid_data.csv"
    insert_csv_file(fname)


main()
