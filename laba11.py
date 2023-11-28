import csv

def readcsv(inputf):
    try:
        with open(inputf, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                if(row[0] == "Population, total"):
                    print(row)
    except FileNotFoundError:
        print(f"File not found: {inputf}")
    except Exception as e:
        print(f"Error reading file: {e}")

def search(inputf, outputf, search_countries):
    try:
        with open(inputf, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            with open(outputf, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                for row in reader:
                    if(row[0] == "Population, total"):
                        if(row[2] in search_countries):
                            writer.writerow(row)
        print("Results written to " + outputf)
    except FileNotFoundError:
        print(f"File not found: {inputf}")
    except Exception as e:
        print(f"Error processing files: {e}")

inputf = "pop.csv"
outputf = "results.csv"

try:
    readcsv(inputf)

    search_countries = input("Enter country names (comma-separated): ").split(',')

    search(inputf, outputf, search_countries)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
