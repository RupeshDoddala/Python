class Employee():
    empCount = 0 #initialization of the data member
    empSal = [];
    empName=[];
    def _init_(self,name,family,salary,department): #default constructor
        self.empname = name
        self.empfamily = family
        self.empsalary = salary
        self.empdepartment = department
        Employee.empCount +=1  #counts the number of employees
        Employee.empSal.append(salary)  #appends salaray attribute
        Employee.empName.append(name)

    def avg_salary(self):
        print('the average salary is')
        sumSal = 0;
        for sal in Employee.empSal:
            sumSal = sumSal+ int(sal);
        return sumSal/len(Employee.empName)

class FulltimeEmployee(Employee):
    def _init_(self,name,family,salary,department):
        Employee._init_(self,name,family,salary,department)


emp1 = FulltimeEmployee('rupesh','doddala','7000','CS');
emp2 = FulltimeEmployee('rahul','yerva','5000','ECE');
emp3 = FulltimeEmployee('nikhil','sanka','4000','CS');
print(FulltimeEmployee.empCount)
print(FulltimeEmployee.empSal)
avgSal = FulltimeEmployee.avg_salary(Employee);
print(avgSal)