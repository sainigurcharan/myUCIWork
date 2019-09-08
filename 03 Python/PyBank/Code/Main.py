import os
import csv
from statistics import mean

#function to return the average of list values
def getAverage(listValues):
    avgChange = round(mean(listValues), 2)
    return avgChange

#funtion to write same print statement to console and text file
def printWriteOutput(printValues, printToValue):
    if (printToValue == "Print"):
        print(printValues)

    elif (printToValue == "File"):
        # Specify the file to write to
        textFilePAth = os.path.join('../Resources', 'PyBank.txt')
        with open(textFilePAth, "w") as textFile:
            textFile.write(printValues)
            textFile.close()

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
    csvReader = csv.reader(csvFile, delimiter=',')
    #Skip the header row
    next(csvReader)
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
    avgChange = getAverage(profitLossList)
    #Print the output as required
    printLines = ""
    printLines += "Financial Analysis \n"
    printLines += "---------------------------------------------------\n"
    printLines += "Total Months: " + str(dataLen+1) + "\n"
    printLines += "Total: $" + str(total) + "\n"
    printLines += "Average Change: $" + str(avgChange) + "\n"
    printLines += "Greatest Increase in Profits: " + str(gIncProfitMonth) + " ($" + str(gIncProfit) + ")\n"
    printLines += "Greatest Decrease in Profits: " + str(gDecProfitMonth) + " ($" + str(gDecProfit) + ")\n"
    printLines += "---------------------------------------------------"

    #Call function to print on console
    printWriteOutput(printLines, "Print")
    # Call function to print on text file
    printWriteOutput(printLines, "File")