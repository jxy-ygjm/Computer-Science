def Unknown(X, Y):
    if X < Y:
        print(X + Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X + Y)
            return int(Unknown(X - 1, Y) / 2)

print(10, 15)
print(Unknown(10, 15))
print(10, 10)
print(Unknown(10, 10))
print(15, 10)
print(Unknown(15, 10))

def IterativeUnknown(X, Y):
    returnValue = 1
    while X != Y:
        print(X + Y)
        if X < Y:
            X = X + 1
            returnValue = returnValue * 2
        else:
            X = X - 1
            returnValue = int(returnValue / 2)
    return returnValue


print(10, 15)
print(IterativeUnknown(10, 15))