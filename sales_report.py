"""Generate sales report showing total melons each salesperson sold."""

# creates empty lists
salespeople = []
melons_sold = []

# opens the sales report file, 
# breaks it down line-by-line, 
# returns a copy of the string with trailing characters removed
# splits the line into elements at the pipe character and assigns them
# to 'entries' variable
f = open('sales-report.txt')
for line in f:
    line = line.rstrip()
    entries = line.split('|')

    salesperson = entries[0] #assigns first element of entries to salesperson variable
    melons = int(entries[2]) #assigns third element of entries to melons variable

    # if the value of salesperson is in the salespeople list,
    #    then the person at specified index of salespeople list is saved to variable 'position'
    if salesperson in salespeople:
        position = salespeople.index(salesperson)

        # increases count of melons_sold at 'position' by amount of 'melons'
        melons_sold[position] += melons
    else: # otherwise:
        salespeople.append(salesperson) # add salesperson to 'salespeople' list
        melons_sold.append(melons) # add 'melons' to melons_sold list

# for each person in salespeople
for i in range(len(salespeople)):
    # print <person> sold <amount of> melons'
    print(f'{salespeople[i]} sold {melons_sold[i]} melons!')
