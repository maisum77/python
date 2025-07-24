age=int(input("enter age= "))
if(age>18):
    print("allowed")
elif(age<18 and age>0):
    print("not allowed")
else:
    print("invalid input")