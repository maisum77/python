class employee():
    def __init__(self):
        print("constructor of employee")
    a=1
class student(employee):
    def __init__(self):
        super().__init__()
        print("constructor of student")
    b=2
class user(student):
    def __init__(self):
        super().__init__()
        print("constructor of user")
    c=3

# e1=employee()
# s1=student()
u1=user()