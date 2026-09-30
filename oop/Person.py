'''
Person class
'''
from os import system
class Person(object):
    
    def __init__(self,lastname:str,firstname:str)->None: 
        self.lastname=lastname
        self.firstname=firstname
        
    def __str__(self)->str:
        return self.lastname+","+self.firstname
        
    def __eq__(self,other:object)->bool:
        if isinstance(other,Person):
            return other.lastname==self.lastname and other.firstname==self.firstname
        
def main()->None:
    system('cls')
    p=Person('durano','dennis')  #instantiate the class Person
    q=Person('durano','dennis')  #instantiate the class Person
    print(p)
    print(q)
    print(f"{p} is equal to {q} is {p.__eq__(q)}")
    
if __name__=="__main__":
    main()