import csv


with open("election_data.csv", "r") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    csv_header = next(csvreader)
    
    candidate = {}
    total_votes = 0
    most_candidate_count = 0
    most_candidate_name = ""  


    for row in csvreader:
        candidate_type = row[2]
        total_votes = total_votes + 1
    
        if candidate_type in candidate:
            candidate[candidate_type] = candidate[candidate_type] +1
        else:  
            candidate[candidate_type] = 1
                
    print(candidate_type)
    print("Elections Results")
    print("-----------------------------")
    print("Total Votes:", total_votes)
    print("-----------------------------")

with open("election_data.csv", "w") as txt_file:    
    output = "candidate\n---------------\n"
    print(output)
    txt_file.write(output + "\n")




    #for key, value in candidate.items():
        #if value > most_candidate_count:
            #most_candidate_name = key
            #most_candidate_count = value
    
        #output = key + ":" + str(value)
    
        #print(output)
        #txt_file.write(output + "\n")
    #print("\nmost votes:")
    #txt_file.write("\nmost votes:")
    
    #output = most_candidate_name + " " + str(most_candidate_count)
    
    #print(output)
    #txt_file.write(output)



    #print("Total:", Total)
   # print("Average Change:", ave)
   # print("Great Increase in Profits:", greatest_date, Greatest_Profit)
    #print("Greastest Decrease in Profits:", least_date, Least_Profit)


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

