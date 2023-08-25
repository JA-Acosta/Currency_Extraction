'''
>>> JAAR
>>> 08/25/2023
>>> Currency Code Extraction
>>> Version 1
'''

'''
>>> Takes a csv file containing information for countries and extracts the three letter currency code as well as the countries name.
'''

import csv

def main() :
    with open('countries.csv', 'r') as csv_country :
        with open('currencies.csv', 'w', newline = '') as csv_currencies :
            countries = csv.DictReader(csv_country)
            fields = ["name", "currencies"]
            csv_writer = csv.DictWriter(csv_currencies, fieldnames = fields)
            for row in countries :
                new_row = { field : row[field] for field in fields }
                csv_writer.writerow(new_row)

if __name__ == '__main__' :
    main()