#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Employee:#Create a data member to count the number of Employees
    employee_count=0
    def __init__(self,name,family,salary,department):#Creating a constructor to initialize name, family, salary, department
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department
        Employee.employee_count=Employee.employee_count+1
    def average_salary(self,employees):#Create a function to average salary
        normal_salary=0
        for i in employees:
            normal_salary=normal_salary+i.salary
        print(normal_salary/len(employees))
class fulltime_employee(Employee):#Creating a Fulltime Employee class and it should inherit the properties of Employee class
            def __init__(self,name,family,salary,department):
                Employee.__init__(self,name,family,salary,department)#Creating the instances of Fulltime Employee class and Employee class and call their member functions.
list=[]
list.append(Employee('Affu','shaik',50000,'informatica'))
list.append(Employee('ferru','kor',80000,'computer Science'))
list.append(Employee('riyaz','md',40000,'Big Data'))

list.append(fulltime_employee('ram ','Boja',60000,'Information Technology'))
list.append(fulltime_employee('vamsi','Kulan',200000,'Oracle'))
list.append(fulltime_employee('viraj ','Boran',80000,'Artificial Intelligence'))


list[0].average_salary(list)
list[2].average_salary(list)
print("number of employees:")
print(Employee.employee_count)
    





import numpy as np
# Create random vector of size 20 with floats between 1 and 20
vec = np.random.uniform(6, 4, 20)
# Reshape the vector to 4 by 5
mat = vec.reshape(4, 5)
# Replacing the max in each row by 0
mat[np.arange(4), mat.argmax(axis=1)] = 0
# Print the output
print(mat)










# In[ ]:




