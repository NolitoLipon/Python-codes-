'''
	DailyEmployee
'''
from Employee import Employee
class DailyEmployee(Employee):
    def __init__(self,idno:str,lastname:str,firstname:str,position:str,rate_per_day:float,days_work:float)->None:
        super().__init__(idno,lastname,firstname,position)
        self.rate_per_day=rate_per_day
        self.days_work=days_work
        
    def __str__(self)->str:
        return f"{super().__str__()},{self.rate_per_day},{self.days_work},{self.computeSalary()}"
     
    def computeSalary(self)->float:
        return self.rate_per_day * self.days_work
     
def main()->None:
    e=DailyEmployee('1000','alpha','bravo','teacher',500.0,10.0)
    f=DailyEmployee('1001','charlie','delta','dean',1000.0,10.0)
    g=DailyEmployee('1002','echo','foxtrot','secretary',600.0,10.0)
    h=DailyEmployee('1003','golf','hotel','chair-person',700.0,10.0)
    print(e)
    print(f)
    print(g)
    print(h)

if __name__=="__main__":
    main()

