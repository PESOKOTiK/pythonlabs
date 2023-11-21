import csv

def readcsv(inputf):
    with open(inputf) as f:
        reader = csv.reader(f)
        for row in reader:
            if(row[0] == "Population, total"):
                print(row)

def search(inputf, outputf, search_countries):
    with open(inputf) as f:
        reader = csv.reader(f)
        with open(outputf, 'w') as f:
            writer = csv.writer(f)
            for row in reader:
                if(row[0] == "Population, total"):
                    if(row[2] in search_countries):
                        writer.writerow(row)

inputf = "pop.csv"
outputf = "results.csv"
readcsv(inputf)

search_countries = input("Enter country names (comma-separated): ").split(',')

search(inputf, outputf, search_countries)
