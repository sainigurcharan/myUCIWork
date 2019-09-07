import os
import csv

csvPath = os.path.join('../Resources', 'budget_data.csv')

# Read in the CSV file
with open(csvPath, 'r') as csvFile:
    # Split the data on commas
    csvReader = csv.reader(csvPath, delimiter=',')
    skipHeader = next(csvReader)

