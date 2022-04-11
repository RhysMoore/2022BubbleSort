def displayList():
    output = "["
    for num in list:
        output += str(num) + ", "
    output += "]"
    print (output)
listToSort = [456, 143, 678, 342, 179, 809, 751, 500]

# Write a loop to split into 2 halves
# Reminder: len(listToSort) to find how many elements are in the list

firstHalf = []
secondHalf = []


for x in range(len(listToSort)-1):
    if(x < len(listToSort)/2):
        firstHalf.append(listToSort[x])
    else:
        secondHalf.append(listToSort[x])

