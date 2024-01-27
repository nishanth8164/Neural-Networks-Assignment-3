class Employee:#Employee class
    empCount=0 ##employeeConut is used to keep track of numner of employee objects
    salSum=0 #salSum is used to take the average of the salaries of the Employee object 
    def __init__(self,name,family,salary,department): #constructor for Employee as per the reuirements
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.empCount += 1
        Employee.salSum+=self.salary
    def avg(self):
        return Employee.salSum/Employee.empCount
    def displayCount(self): #One of the functions in Employee class
        print ("Total Employee %d" % Employee.empCount)
    def displayEmployee(self):#another function for employee class
        print("Name : ", self.name, "Family: ", self.family , "Salary: ", self.salary, "department:",self.department)

emp1 = Employee("srinivas","reddy",2000,"support")#Employee objects creation with intialization
emp2 = Employee("jahnavi","saripalli",5000,"transport")
print("avg:",emp2.avg())#calling average function
class FulltimeEmployee(Employee):#FulltimeEmployee class with Employee as its parent class
    def __init__(self,name,family,salary,department,c_name):#constructor for FulltimeEmployee
        super().__init__(name,family,salary,department)
        self.c_name=c_name
    def setCompany(self,c_name):#one of the FulltimeEmployee class function
        self.c_name=c_name
    def getCompany(self):
        if self.c_name not in self.c_name:
            return ""
        return self.c_name
adi=FulltimeEmployee("Nishanth","Sri Harsha",75000,"FULL-STACK","WIPRO")#FultimeEmployee object
adi.setCompany("Apple")#calling the member functions of FulltimeEmploye and Employee
adi.getCompany(),adi.displayEmployee(),emp1.displayCount()
