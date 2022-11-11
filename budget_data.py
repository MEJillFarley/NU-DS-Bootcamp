import csv

with open("budget_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    Row = next(csvreader)

    Rowcount = 1
    Total = 0
    Total = float(Total) + float(Row[1])
    Greatest_Profit = 0
    Least_Profit = 0
    greatest_date = Row[0]
    least_date = Row[0]
    prev = Row

    for row in csvreader:
        Rowcount = Rowcount + 1
        Total = float(Total) + float(row[1])
        diff = float(row[1]) - float(prev[1])
        #ave = diff / Rowcount
        if Greatest_Profit < diff:
            Greatest_Profit = diff
            greatest_date = row[0]
        if Least_Profit > diff:
            Least_Profit = diff
            least_date = row[0]
        prev = row
    print("Total Months:", Rowcount)
    print("Total:", Total)
    #print("Average Change:", ave)
    print("Great Increase in Profits:", greatest_date, Greatest_Profit)
    print("Greastest Decrease in Profits:", least_date, Least_Profit)


#print(row[0])
        #print(row[1])
        #Date = row[0]
        #Budget = row[1]
        #Rowcount+=1
        #print("Number of Months:", Rowcount)

# Month Count
#def average(numbers):

    #total = 0.0
    #for number in numbers:
        #total += number
        #return total / len(numbers)
    #print("Total Lines:", total)


#print("Total Months:", str(Date))
#counter = 0
#for i in Date:
#Months = Months + 1
#print("Total Months:" + str(counter))

#len(row[0])
#Months = row[0]
#print("Total Months:",len(Date))



   





