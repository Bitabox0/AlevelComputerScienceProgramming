# [a, b, c]

answers = [
    [True, False, False],
    [False, True, False],
    [False, False, True],
    [True, False, False],
    [True, False, False],
    [True, False, False],
    [False, True, False],
    [False, False, True],
    [True, False, False],
    [True, False, False],
]

counta = 0
countb = 0
countc = 0

for i in range(0, len(answers)):
    if answers[i][0] == True:
        counta =+ 1
    elif answers[i][1] == True:
        countb =+ 1
    elif answers[i][2] == True:
        countc =+ 1