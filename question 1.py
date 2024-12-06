class node:
    def __init__(self, data, nextNode):
        self.data = data
        self.nextNode = nextNode

linkedList = [node(1, 1), node(5,4), node(6,7), node(7, -1), node(2, 2), node(0, 6), node(0, 6), node(0, 8), node(56, 3), node(0, 9), node(0, -1)]
# DECLARE startPointer, pointer: INTEGER

def outputNodes(linkedList, startPointer):
    print(linkedList[startPointer].data)
    if linkedList[startPointer].nextNode != -1:
        outputNodes(linkedList, linkedList[startPointer].nextNode)

startPointer = 0
outputNodes(linkedList, startPointer)

emptyList = 5
def addNode(linkedList, startPointer):
    global emptyList
    if emptyList == -1:
        return False
    else:
        data = int(input("Enter the data to be input: "))
        while linkedList[startPointer].nextNode != -1:
            startPointer = linkedList[startPointer].nextNode
        linkedList[startPointer].nextNode = emptyList
        linkedList[emptyList].data = data
        temporary = linkedList[emptyList].nextNode
        linkedList[emptyList].nextNode = -1
        emptyList = temporary
        return True

outputNodes(linkedList, startPointer)
if addNode(linkedList, startPointer):
    print("Node added successfully")
else:
    print("Node not added")
outputNodes(linkedList, startPointer)
