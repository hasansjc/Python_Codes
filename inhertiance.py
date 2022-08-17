import classes


class Programmer(classes.Student):
    
    def __init__(self, name,age,prg_language):
        super().__init__(name,age)
        self.lang = prg_language
    
    def print_info(self):
        
        super().print_info()
        print("You like " + self.lang," programming language ",)
         
p1 = Programmer("ahmed",26, "Python")

p1.print_info()