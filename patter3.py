rows=int(input("enter the limit:"))
for i in range(1,rows+1): #outer loops for rows
    for j in range(rows-i): #inner loop for spaces
        print(" ",end="")
    for k in range(2*i-1): #inner loops for stars
        print("*",end="")
    print()





