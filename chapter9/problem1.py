with open("poem.txt") as str:
    a=str.read()
if("twinkle" in a):
    print("present in the string")
else:
    print("not present in the string") 