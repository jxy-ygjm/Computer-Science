class TreasureCheat:
    def __init__(self, question, answer, points):
        # DEFINE question, answer: STRING
        # DEFINE points: INTEGER
        self.__question = question
        self.__answer = answer
        self.__points = points

    def getQuestion(self):
        return self.__question

    def checkAnswer(self, answer):
        if answer == self.__answer:
            return True
        else:
            return False

    def getPoints(self, numOfAttempt):
        if numOfAttempt == 1:
            return self.__points
        elif numOfAttempt == 2:
            return self.__points / 2
        elif numOfAttempt == 3 or numOfAttempt == 4:
            return self.__points / 4
        else:
            return 0

def readData():
    try:
        myFile = open("TreasureChestData.txt", "r")
        step = 0
        global arrayTreasure
        myTreasureCheat = TreasureCheat
        question = ''
        answer = ''
        points = 0
        for myLine in myFile:
            step += 1
            myLine = myLine.strip()
            if step == 1:
                question = myLine
            elif step == 2:
                answer = int(myLine)
            else:
                points = int(myLine)
                arrayTreasure.append(myTreasureCheat(question, answer, points))
                step = 0
        myFile.close()
    except FileNotFoundError:
        print("File not found")

arrayTreasure = []
readData()
questionNum = int(input("Which question do you want to answer: "))
myTreasureCheat = arrayTreasure[questionNum - 1]
print(myTreasureCheat.getQuestion())
numOfAttemp = 1
answerWrong = True
while answerWrong:
    answer = int(input("Please enter your answer: "))
    if myTreasureCheat.checkAnswer(answer):
        print("You award: ", myTreasureCheat.getPoints(numOfAttemp))
        answerWrong = False
        break
    else:
        numOfAttemp += 1