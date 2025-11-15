commad=input("Enter your query: ")
id={
    101:"shipped",
    102:"in progress"
}

if commad in ["track","order","track order"]:
    temp=int(input("Enter your product id: "))
    for i in id:
        if(temp==i):
            print(f"Your order is in {id[i]}")
elif commad in ["cencel"]:
    temp=input("Reason for cencelation of order: ")
    print("Order ceneclation successfully ")
elif commad in ["return"]:
    temp=int(input("Enter your product id: "))
    print(f"order return initiated: {temp}")


    