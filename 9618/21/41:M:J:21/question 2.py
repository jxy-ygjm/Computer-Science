# DECLARE arrayData: ARRAY[0:9] OF INTEGER
arrayData = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linearSearch(searchData):
    for i in range(len(arrayData)):
        if arrayData[i] == searchData:
            return True
    return False

searchData = int(input("Enter a number to be searched: "))
if linearSearch(arrayData):
    print("Found")
else:
    print("Not Found")

def bubbleSort():
    for x in range(len(arrayData)):
        for y in range(len(arrayData) - 1):
            if arrayData[y] < arrayData[y + 1]:
                temp = arrayData[y]
                arrayData[y] = arrayData[y + 1]
                arrayData[y + 1] = temp