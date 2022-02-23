import csv
from pathlib import Path
menu = Path('../PyRamen/menu_data.csv')
with open (menu, 'r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)

    items = []
    for line in csv_reader:
        items.append(line[0])
    print(items)