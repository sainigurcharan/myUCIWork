import os
import csv

#funtion to write same print statement to console and text file
def printWriteOutput(printValues, printToValue):
    if (printToValue == "Print"):
        print(printValues)

    elif (printToValue == "File"):
        # Specify the file to write to
        textFilePAth = os.path.join('../Resources', 'PyPoll.txt')
        with open(textFilePAth,"w") as textFile:
            textFile.write(printValues)
            textFile.close()

#set csv path
csvPath = os.path.join('../Resources', 'election_data.csv')

#initialize the variables
candidateVotes = 0
totalVotes = 0
winnerPercent = 0.0
winnerCandidate = ""
# dictionary for name: List
pollCandidate = {}

# Read in the CSV file
with open(csvPath, newline = "") as csvFile:
    csvReader = csv.reader(csvFile, delimiter=',')
    # Skip the header row
    next(csvReader)
    for curRow in csvReader:
        totalVotes += 1
        #Checking data for each candidate and updating his/her vote count
        if curRow[2] in pollCandidate.keys():
            candidateVotes = pollCandidate[curRow[2]] + 1

        else:
            candidateVotes = 1
        #updating candidate data in a dictionary
        pollCandidate.update({curRow[2]: int(candidateVotes)})

    printLines = ""
    printLines += "Election Results \n"
    printLines += "------------------------- \n"
    printLines += "Total Votes: " + str(totalVotes) + "\n"
    printLines += "------------------------- \n"
    #Manipulating each candidate vote count and win percentage
    for dictRow in pollCandidate:
        #manipulating the win percentage
        if winnerPercent < round((pollCandidate[dictRow]/totalVotes) * 100, 3):
            winnerPercent = round((pollCandidate[dictRow]/totalVotes) * 100, 3)
            winnerCandidate = dictRow

        printLines += str(dictRow) + ": " + str(round((pollCandidate[dictRow]/totalVotes) * 100, 3)) + "% (" + str(pollCandidate[dictRow]) + ")\n"
    # Print the output as required
    printLines += "------------------------- \n"
    printLines += "Winner: " + winnerCandidate + "\n"
    printLines += "------------------------- \n"
    # Call function to print on console
    printWriteOutput(printLines, "Print")
    # Call function to print on text file
    printWriteOutput(printLines, "File")