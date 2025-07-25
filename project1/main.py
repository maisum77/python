import random
rand_number = random.randint(1, 3)
dic={
    1:"snake",
    2:"gun",
    3:"water"
}
comp_element=dic[rand_number]
# print(comp_element)
print("""elements
      1=snake
      2=gun
      3=water""")
temp=int(input("enter your element="))
user=dic[temp]
if(comp_element=="snake" and user=="gun"):
    print("gun kill the snake")
elif(comp_element=="snake" and user=="water"):
    print("snake drink the water")
elif(comp_element=="snake" and user=="snake"):
    print("Tie")
elif(comp_element=="gun" and user=="snake"):
    print("gun kill the snake")
elif(comp_element=="gun" and user=="water"):
    print("water has no effect on the gun")
elif(comp_element=="gun" and user=="gun"):
    print("tie")
elif(comp_element=="water" and user=="snake"):
    print("snake drink the water")
elif(comp_element=="water" and user=="water"):
    print("tie")
elif(comp_element=="water" and user=="gun"):
    print("gun has no effect on the gun")

