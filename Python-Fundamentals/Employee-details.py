'''Program to create a class Employee with empno,name,depname,designation,age and salry and perform the following function.
   a.To accept details of n Employees.
   b.To display details of all employess.
   c.To search for an employee and display the details of that employee.'''
class Employee:
 def __init__(self,empno,name,depname,designation,age,salary):
    self.empno=empno
    self.name=name
    self.depname=depname
    self.designation=designation
    self.age=age
    self.salary=salary

 def display(self):
    print('-'*25)
    print("Employee No:",self.empno)
    print("Name:",self.name)
    print("Department:",self.depname)
    print("Designation:",self.designation)
    print("Age:",self.age)
    print("Salary:",self.salary)

employees=[]
n=int(input("Enter the number of Employees:"))

for i in range(n):
      print(f"\nEnter details of employee{i+1}:")
      empno=int(input("Enter Employee No:"))
      name=input("Enter Name:")
      depname=input("Enter Department:")
      designation=input("Enter Designation:")
      age=int(input("Enter Age:"))
      salary=int(input("Enter Salary:"))
      emp=Employee(empno,name,depname,designation,age,salary)
      employees.append(emp)
      
      
print("\n Employee Details:")
for emp in employees:
    emp.display()

search_empno=int(input("Enter Employee number to search:"))
found=False

for emp in employees:
            if emp.empno==search_empno:
              print("\nEmployee found")
              emp.display()
              found=True
              break

if not found:
    print("\nEmployee not found!!")
                 
      
      
      
