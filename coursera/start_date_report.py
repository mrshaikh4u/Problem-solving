#!/usr/bin/env python3
import csv
import datetime
import requests
from collections import defaultdict

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():
    """Interactively get the start date to query for."""

    print()
    print('Getting the first start date to query for.')
    print()
    print('The date must be greater than Jan 1st, 2018')
    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    print()
    return datetime.datetime(year, month, day)

def get_file_lines(url):
    """Returns the lines contained in the file at the given URL"""

    # Download the file over the internet
    response = requests.get(url, stream=True)

    # Decode all lines into strings
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

def get_same_or_newer(start_date):
    """Returns the employees that started on the given date, or the closest one."""
    data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    date_employee_map = defaultdict(list)
    for row in reader:
        current_data = []
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        name = "{} {}".format(row[0], row[1])
        if row_date in date_employee_map:
            current_data = date_employee_map.get(row_date)
        current_data.append(name)
        date_employee_map[row_date] = current_data

    for k in sorted(date_employee_map):
        if k < start_date:
            continue
        break
    return k,date_employee_map.get(k)


def list_newer(start_date):
    print("got start date as : ",start_date)
    while start_date < datetime.datetime.today():
        start_date, employees = get_same_or_newer(start_date)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))

        # Now move the date to the next one
        start_date = start_date + datetime.timedelta(days=1)

def main():
    start_date = get_start_date()
    list_newer(start_date)

if __name__ == "__main__":
    main()
