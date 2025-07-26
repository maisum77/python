class employee:
    def __init__(self,name):
        self.name=name
    company="systems"
    def show(self):
        print(f"name is {self.name},and company name is {self.company}\n")
class programmer(employee):
    company="devini"
    code="python"
    def coding(self):
        print(f"this employee hate coding {self.code}\n")

a=employee("maisum")
b=programmer("ali")
a.show()
b.show()
b.coding()