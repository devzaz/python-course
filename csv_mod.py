import csv

with open('people_data.csv', 'r') as rf:
    reader = csv.reader(rf, delimiter=" ", quotechar='|')

    for row in reader:
        print('||'.join(row))
