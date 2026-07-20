num=int(input("Enter a number: "))
if num<=0:
    print("Please enter a valid number")
else:
    for i in range(1,num+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()