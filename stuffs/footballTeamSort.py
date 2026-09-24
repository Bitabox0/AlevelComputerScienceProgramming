teams = ["Everton", "Liverpool", "Manchester united", "Hull", "Fulham", "Aston Villa", "Chelsea", "Brighton", "West Ham"]
points = [102, 3, 68, 98, 69, 32, 65, 45, 86]
print(teams)

# for i in range(0, len(teams)):
#     inpScore = input("enter points for " + teams[i] + ": ")

for i in range(0, len(teams)):
    print(teams[i] + ": " + str(points[i]) + " points")

highest = 0
for i in range(0, len(teams)):
    if points[i] > highest:
        highest = points[i]
        winningIndex = i
print(teams[winningIndex] + " is the winner")

sortChoice = int(input("""how would you like the teams to be displayed: 
1) sort by alphibetical
2) sort by points
3) quit
: """))

match sortChoice:
    case 1:
        swapped = True

        while swapped == True:
            swapped = False
            for i in range(0, len(teams)-1):
                if teams[i] > teams[i+1]:
                    temp = teams[i]
                    teams[i] = teams[i+1]
                    teams[i+1] = temp
                    swapped = True   
        print(teams)
    case 2:
        swapped = True
        
        while swapped == True:
            swapped = False
            for i in range(0, len(points)-1):
                if points[i] > points[i+1]:
                    temp = points[i]
                    points[i] = points[i+1]
                    points[i+1] = temp
                    temp2 = teams[i]
                    teams[i] = teams[i+1]
                    teams[i+1] = temp2
                    swapped = True
        for i in range(0, len(points)):
            print(teams[i] + ": " + str(points[i]) + " points")

    case 3:
        print("up the toffies!!!!! scram kid... heh")