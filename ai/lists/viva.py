import random
def check(student):
    status=random.choice(['viva done','viva pending'])
    if status == 'viva done':
        print(f"viva of the {student} is done already")
    else:
        print(f"viva of the {student} is pending ")

def main():
    a=input("enter student name: ")
    check(a)

if __name__=="__main__":
    main()