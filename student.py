class Student:
    def __init__(self,first_name,last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
    def greeting(self):
        return f"Hello {self.name} from {self.country}" 
    def full_name(self):
        return f"Hello {self.first_name} {self.last_name}" 
    def year_of_birth(self):
        return f"you were born in {2022-self.age} which makes you {self.age} years old"
    def initials(self):
        return f"Hello {self.first_name[0]} {self.last_name[0]} from{self.country} you were born in exwhich makes you {self.age} years old"

        
    


   