import random
import string

charValues = string.ascii_letters +  string.digits + string.punctuation

while True :
        print("Enter Password Length : ")
        len = input()
        try :
            len=int(len)
        except:
            print("Please Enter Length in Digits Only")
            continue
        if len<6:
            print("Length Must be greater than six")
            continue
        break

pw = "".join([random.choice(charValues) for i in range(len)])

print("your password  is : ",pw)
