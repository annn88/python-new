def valid_number():
    num=input("enter a number:")
    if len(num)==10 and num[0]in"9,8,7":
        print("it is a valid number")
    else:
        print(" the number is invalid")
valid_number()

