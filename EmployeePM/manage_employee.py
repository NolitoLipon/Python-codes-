from DailyEmployee import DailyEmployee
from MonthlyEmployee import MonthlyEmployee
from os import system

dailyemployee:list = []
monthlyemployee:list = []

idno:str = None
lastname:str = None
firstname:str = None
position:str = None
dailyrate:float = 0.0
monthlyrate:float = 0.0
emptype:str=None

def employeeform(title:str)->None:
    def decorator(func)->None:
        def wrapper()->None:
            global idno,lastname,firstname,position
            system('cls')
            print(title.upper().center(40,'-'))
            idno = input('IDNO      :')
            lastname = input('LASTNAME  :')
            firstname = input('FIRSTNAME :')
            position = input('POSITION  :')
            func()
        return wrapper
    return decorator
@employeeform('add employee')
def add_employee()->None:
    emptype = input("(D)aily (M)ontly :").upper() 
    if emptype == 'D':
        dailyrate = float(input("DAILY RATE :"))
        daily_employee:Employee = DailyEmployee(idno,lastname,firstname,position,dailyrate,0)
        dailyemployee.append(daily_employee)
    if emptype == 'M':
        monthlyrate = float(input("MONTHLY RATE :"))
        monthly_employee:Employee = MonthlyEmployee(idno,lastname,firstname,position,monthlyrate,0)
        monthlyemployee.append(monthly_employee)
    
    
def find_employee()->None:pass
def delete_employee()->None:pass
def update_employee()->None:pass
def displayall_employee()->None:
    system('cls')
    print("DAILY EMPLOYEE")
    if len(dailyemployee)>0:
        for emp in dailyemployee:
            print(emp)
    else:print("Daily employee list is empty!")
    print("-"*40)
    print("MONTHLY EMPLOYEE")
    if len(monthlyemployee)>0:
        for emp in monthlyemployee:
            print(emp)
    else:print("Monthly employee list is empty!")
#
def menu()->None:
    system('cls')
    print('MANAGE EMPLOYEE'.center(40,'-'))
    print('1. ADD EMPLOYEE')
    print('2. FIND EMPLOYEE')
    print('3. DELETE EMPLOYEE')
    print('4. UPDATE EMPLOYEE')
    print('5. DISPLAY ALL EMPLOYEE')
    print("-"*40)
    
def main()->None:
    option:int = 9999
    while option != 0:
        menu()
        try:
            option = int(input("Enter Option(0..5):"))
            if   option == 1: add_employee()
            elif option == 2: find_employee()
            elif option == 3: delete_employee()
            elif option == 4: update_employee()
            elif option == 5: displayall_employee()
            elif option == 0: print("program ends...")
            
        except Exception as e:
            print("Invalid Input :{e}")
        
        input("\nPress any key to continue...")
        
if __name__=="__main__":
    main()
    
    
    
    
    
