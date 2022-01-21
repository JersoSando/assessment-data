log_file = open("um-server-01.txt") #importing the um-server-01.text file and saving it to a variable


def sales_reports(log_file): #creating a function called sales_reports and having it take in a parameter log_file
    for line in log_file: #looping over each line of a file (loop over list)
        line = line.rstrip() #gets rid of all the whitespace
        day = line[0:3] #checks the first 3 letters of the list and returns a string
        if day == "Mon": #if the day (the first three letters) is Tue
            print(line) #print the line 'Tue' as a string


sales_reports(log_file)#invokes the sales_reports function


def melon_orders(log_file):
    for line in log_file:
        line = line.rstrip().split('')
        count = int(line[2])
        if count > 10:
            print(line)

melon_orders(log_file)