parking = [["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"],
        ["empty", "empty", "empty", "empty", "empty", "empty"]]

YgridRef = int(input("enter the row the car was parked: "))
XgridRef = int(input("enter the Column the car was parked: "))
while YgridRef > 10 or XgridRef > 6 or parking[YgridRef-1][XgridRef-1] != "empty":
    YgridRef = int(input("invalid, re-enter the row the car was parked: "))
    XgridRef = int(input("invalid, re-enter the Column the car was parked: "))
regNum = input("enter the registration number or the car: ")
parking[YgridRef-1][XgridRef-1] = regNum
for i in range(0, len(parking)):
    print(parking[i])