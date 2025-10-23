scrabbleInput = input("enter your letter: ")
def scrabbleScores(scrabbleInput):
    onePoint = ["a","e","i","o","u","l","n","r","s","t"]
    twoPoint = ["d","g"]
    threePoint = ["b","c","m","p"]
    fourPoint = ["f","h","w","y","v"]
    fivePoint = ["k"]
    eightPoint = ["j","x"]
    tenPoint = ["q","z"]
    letterFound = False
    while letterFound == False:
        for i in onePoint:
            if i == scrabbleInput.lower():
                print("this is worth one point")
                letterFound = True
            else:
                next
        for i in twoPoint:
            if i == scrabbleInput.lower():
                print("this is worth two points")
                letterFound = True
            else:
                next
        for i in threePoint:
            if i == scrabbleInput.lower():
                print("you get three points")
                letterFound = True
            else:
                next
        for i in fourPoint:
            if i == scrabbleInput.lower():
                print("this is worth four points")
                letterFound = True
            else:
                next
        for i in fivePoint:
            if i == scrabbleInput.lower():
                print("this is worth five points")
                letterFound = True
            else:
                next
        for i in eightPoint:
            if i == scrabbleInput.lower():
                print("this is worth eight points")
                letterFound = True
            else:
                next
        for i in tenPoint:
            if i == scrabbleInput.lower():
                print("this is worth ten points")
                letterFound = True
            else:
                next    
scrabbleScores(scrabbleInput)
