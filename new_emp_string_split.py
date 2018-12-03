class Employee:
  
   num_of_emps = 0
   raise_amount = 1.04   #class variable
   
   def __init__(self, first, last, pay):
     #instances
       self.first = first                         
       self.last  = last
       self.pay   = pay
       self.email = first + '.' + last + '@company.com'
       
       Employee.num_of_emps += 1 #create new employee
       
   def fullname(self):
       return '{} {}'.format(self.first, self.last)
       
       
       
   def apply_raise(self):   #method
       self.pay = int(self.pay * Employee.apply_raise)
       
   @classmethod
   def set_raise_amt(cls, amount):
       cls.raise_amt = amount
     
       
       
       
 
emp_1 = Employee('Corey', 'Schafer', 5000)
emp_2 = Employee('Test', 'User', 6000)
 
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-5000'
emp_str_3 = 'Bubu-Bim-45000'

first, last, pay = emp_str_1.split('-')

new_emp_1 = Employee(first, last, pay)

print(new_emp_1.email)
print(new_emp_1.pay)












 
 