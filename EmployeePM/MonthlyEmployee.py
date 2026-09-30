'''
	DailyEmployee
'''
from Employee import Employee
class MonthlyEmployee(Employee):
    def __init__(self,idno:str,lastname:str,firstname:str,position:str,rate_per_month:float,days_work:float)->None:
        super().__init__(idno,lastname,firstname,position)
        self.rate_per_month=rate_per_month
        self.days_work=days_work
        
    def __str__(self)->str:
        return f"{super().__str__()},{self.rate_per_month},{self.days_work},{self.computeSalary()}"
     
    def computeSalary(self)->float:
        return  ((self.rate_per_month/20)*self.days_work)
     
def main()->None:
    e=MonthlyEmployee('1000','alpha','bravo','teacher',10000.0,20.0)
    f=MonthlyEmployee('1001','charlie','delta','dean',15000.0,18.0)
    g=MonthlyEmployee('1002','echo','foxtrot','secretary',20000.0,17.0)
    h=MonthlyEmployee('1003','golf','hotel','chair-person',18000.0,19.0)
    print(e)
    print(f)
    print(g)
    print(h)

if __name__=="__main__":
    main()

