string, lst = " ", []   




class Person:   

    nationality = "Indian" 

    def __init__(self, name, age, sex, city): 
        self.name = name
  
        self.age = age
        self.sex = sex
        self.city = city  

    def person_bio(self):
        bio = f'{self.name} is {self.age} years old living in {self.city} and {self.name} is a {self.sex}'
        return bio

    def eligibility(self):  
        if self.age >= 18:
            return f'{self.name} is eligible'
        else:
            return f'{self.name} is not eligible'




person1 = Person('Surya', 19, 'male', 'Chennai')   
person2 = Person('ravi', 14, 'female', 'Hyderabad')  

Person.nationality = "African" 
person1.nationality = "Indian"  

person1.name  
person1.person_bio()  