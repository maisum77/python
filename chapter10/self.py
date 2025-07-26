class employee:
    name="maisum"
    language="python"

    def get_info(self):
        print(f"the language is {self.language}")
    
    @staticmethod
    def greet():
        print("hello how you doing !!")
    

e1=employee()
e1.get_info()
e1.greet()