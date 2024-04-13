class person:

   def __init__(self,name,age,salary):

      self.naam=name
      self.earning=salary
      self.age=age
      self.standard=None


   def print_name_age_salary(self):
      print("name={},age={},salary={},standard=".format(self.naam,self.earning,self.age,self.standard))

   def a(self):
      print("hi",self.age)

emp1=person("mayank",25,1200000)
emp2=person("a",29,1000000)

emp1.standard=9

emp1.print_name_age_salary()
print("name=",emp2.naam,end="")
print(",salary=",emp2.earning,end="")
print(",age=",emp2.age)

class B(person):
   pass

x=B("b",24,100)

x.print_name_age_salary()

emp2.a()

print(emp1.standard)