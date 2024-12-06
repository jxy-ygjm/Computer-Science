class Picture:
    def __init__(self, Description, Width, Height, FrameColour):
        # DECLARE Description, FrameColour: STRING
        # DECLARE Width, Height: INTEGER
        self.__Description = Description
        self.__Width = Width
        self.__Height = Height
        self.__FrameColour = FrameColour

    def GetDescription(self):
        return self.__Description

    def GetHeight(self):
        return self.__Height

    def GetWidth(self):
        return self.__Width

    def GetColour(self):
        return self.__FrameColour

    def SetDescription(self, NewDescription):
        self.__Description = NewDescription

pictureArray = []
for i in range(100):
    pictureArray.append(Picture("", 0, 0, ""))

def ReadData():
    global pictureArray
    try:
        myFile = open("Pictures.txt", "r")
        step = 0
        total = 0
        Description = ""
        Width = 0
        Height = 0
        FrameColour = ""

        for line in myFile:
            step += 1
            if step == 1:
                Description = line.strip().lower()
            elif step == 2:
                Width = int(line.strip())
            elif step == 3:
                Height = int(line.strip())
            else:
                FrameColour = line.strip().lower()
                step = 0
                pictureArray[total] = Picture(Description, Width, Height, FrameColour)
                total += 1
    except FileNotFoundError:
        print("File Not Found")

ReadData()
requirementColour = input("Enter the requirements colour: ").lower()
requirementWidth = int(input("Enter the requirements width: "))
requirementHeight = int(input("Enter the requirements height: "))
for myPicture in pictureArray:
    if myPicture.GetColour() == requirementColour and myPicture.GetWidth() <= requirementWidth and myPicture.GetHeight() <= requirementHeight:
        print(myPicture.GetDescription(), myPicture.GetWidth(), myPicture.GetHeight())