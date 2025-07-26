class employee():
    def __init__(self,name,language):
        self.name=name
        self.language=language
        print("creating the object")

maisum=employee("maisum","python")
print(maisum.name)
print(maisum.language)