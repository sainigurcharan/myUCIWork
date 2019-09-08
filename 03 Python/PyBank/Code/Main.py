import os
import csv
from statistics import mean
#set csv path
csvPath = os.path.join('../Resources', 'budget_data.csv')

#initialize the variables
total = 0
avgChange = 0.0
gIncProfitMonth = ""
gIncProfit = 0
gDecProfitMonth = ""
gDecProfit = 0
dataLen = 0
profitLossList = []

# Read in the CSV file
with open(csvPath, 'r', newline='') as csvFile:
    # Split the data on commas
    csvReader = csv.reader(csvFile, delimiter=',')
    #Skip the header row
    skipHeader = next(csvReader)
    #get previous row
    prevRow = next(csvReader)
    #add into total for the previous row
    total = int(prevRow[1])
    #loop through all the rows in the csv
    for curRow in csvReader:
        #total of Profit/Loss
        total = total + int(curRow[1])
        #Average change between previous and current row Profit/Loss
        avgChange = float(curRow[1]) - float(prevRow[1])
        #Append the data into List for manipulations
        profitLossList.append(avgChange)
        #Check for greatest increase and decrease of average change between values
        if profitLossList[dataLen] > gIncProfit:
            gIncProfitMonth = curRow[0]
            gIncProfit = int(profitLossList[dataLen])
        if profitLossList[dataLen] < gDecProfit:
            gDecProfitMonth = curRow[0]
            gDecProfit = int(profitLossList[dataLen])
        prevRow = curRow
        dataLen += 1
    #Average change
    avgChange = round(mean(profitLossList), 2)
    #Print the output as required
    print("Financial Analysis")
    print("---------------------------------------------------")
    print(f"Total Months: {dataLen+1}")
    print(f"Total: ${total}")
    print(f"Average Change: ${avgChange}")
    print(f"Greatest Increase in Profits: {gIncProfitMonth} (${gIncProfit})")
    print(f"Greatest Decrease in Profits: {gDecProfitMonth} (${gDecProfit})")
    print("---------------------------------------------------")

# Specify the file to write to
textFilePAth = os.path.join('../Resources', 'PyBank.txt')
textFile = open(textFilePAth,"w")
textFile.write("Financial Analysis \n")
textFile.write("---------------------------------------------------\n")
textFile.write(f"Total Months: {dataLen+1}\n")
textFile.write(f"Total: ${total}\n")
textFile.write(f"Average Change: ${avgChange}\n")
textFile.write(f"Greatest Increase in Profits: {gIncProfitMonth} (${gIncProfit})\n")
textFile.write(f"Greatest Decrease in Profits: {gDecProfitMonth} (${gDecProfit})\n")
textFile.write("---------------------------------------------------")
textFile.close()