def getPword(attempt):    
    if attempt == 1:
        password1 = input("please enter your password: ")
        while len(password1) < 6 or len(password1) > 8:
            password1 = input("password is not 6 to 8 characters long, please re-enter your password: ")
        attempt = 2
        
    if attempt == 2:
        password2 = input("please re-enter your original password: ")
        while len(password2) < 6 or len(password2) > 8:
            password2 = input("password is not 6 to 8 characters long, please re-enter your password: ")
    return password1, password2

#>-------------------------------------------------------------<#

attempt = 1
password1, password2 = getPword(attempt)
if password1 == password2:
    print("passwords match!")
else:
    print("passwords dont match! please try again")
    getPword(attempt)