# name=input("enter name= ")
# file=open("names.txt","a")
# file.write(f"{name}\n")
# file.close()

# in this we dont have to close the file explicitly
# name=input("enter name= ")
# with open("names.txt","a") as file:
#     file.write(f"{name}\n")


# with open("names.txt","r") as file:
#     lines=file.readlines()
# for line in lines:
#     print(f"hello,{line}",line.rstrip())

# names=[]
# with open("names.txt","r") as file:
#     for line in file:
#         names.append(line.rstrip())
# for line in sorted(names):
#     print(f"Hello {line}")

# names=[]
# with open("names.txt","r") as file:
#     for line in sorted(file):
#         print(f"Hello {line.rstrip()}",)

# with open("students.csv","r") as file:
#     for line in file:
#         row=line.rstrip().split(",")
#         print(f"The {row[0]} is in the {row[1]} department")
    
# studnets=[]
# with open("students.csv","r") as file:
#     for line in file:
#         name,house =line.rstrip().split(",")
#         student={}
#         student["name"]=name
#         student["house"]=house
#         studnets.append(student)

# def get_student(students):
#     return students['name']

# for student in sorted(studnets,key=get_student):
#     print(f"Student={student['name']} department={student['house']}")

import csv
studnets=[]
with open("students.csv") as file:
    for line in file:
        reader=csv.reader(file)
        for row in reader:
            studnets.append({"name":row[0],"dept":row[1]})


    
def get_student(students):
    return students['name']

for student in sorted(studnets,key=get_student):
    print(f"Student={student['name']} department={student['dept']}")

    
 