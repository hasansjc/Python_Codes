
class Student:
    
    def __init__(self,name,age):
        
        self.name = name
        self.age = age
    
    def print_info(self):              # self argument is compulsory in all the functions.
        
        print(f" Your name is {self.name} and your age is {self.age}")
        
    def update_info(self, new_name, new_age):
        self.name = new_name
        self.age = new_age


if(__name__ == '__main__'):
    s1 = Student("ahmed",27)
    s1.print_info()

    s1.update_info("hasan",28)
    s1.print_info()
