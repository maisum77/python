class Student:
    def __init__(self,name,house):
        self.name=name
        self.house=house
        
        if not name:
            raise ValueError("missing name")
    def __str__(self):
        return "a student"
    
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self,name):
        self._name=name




    #getter
    @property
    def house(self):
        return self._house
    #setter
    @house.setter
    def house(self,house):
        self._house=house





def main():
    students=get_student()
    # print(f"{students.name} and the house are {students.house}")
    print(students)

def get_student():
    # name=input("enter the name= ")
    # house=input("enter the house= ")
    # return {"name":name,"house":house}
    # student=Student()
    # student.name=input("enter the name= ")
    # student.house=input("enter the house= ")
    # return student
    name=input("enter the name= ")
    house=input("enter the house= ")
    return Student(name,house)

if __name__== "__main__":
    main()