daysOfTheWeek = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"] 

people = ["Matt", "Arif", "Billy", "Daniel", "Ivan", "Oskar", "Emily", "Philip", "Eva", "Sasha"]

scores = [
    [40, 21, 43, 65, 20, 34, 43],
    [33, 83, 63, 65, 41, 24, 54],
    [13, 21, 48, 25, 20, 34, 62],
    [33, 51, 36, 67, 21, 54, 12],
    [73, 21, 43, 65, 70, 34, 78],
    [33, 21, 48, 61, 20, 38, 98],
    [23, 24, 43, 65, 37, 34, 56],
    [33, 23, 53, 63, 20, 34, 12],
    [37, 21, 43, 35, 46, 34, 67],
    [33, 51, 63, 65, 23, 34, 84],
]
def getScores():
    for i in range(len(people)):
        print("<" + people[i] + ">") 
        for j in range(len(scores[0])):
                print(daysOfTheWeek[j] + ": " + str(scores[i][j]))


for i in range(len(people)):
      print(str(i + 1) + ": " + people[i])

studentInfo = int(input("enter number of student: "))
print(people[studentInfo - 1] + " - " + str(scores[studentInfo - 1]))
