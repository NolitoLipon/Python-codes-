'''
	Employee class
'''
from Person import Person
from abc import ABC,abstractmethod
class Employee(Person,ABC):
    def __init__(self,idno:str,lastname:str,firstname:str,position:str)->None:
        super().__init__(lastname,firstname)
        self.idno = idno
        self.position = position
        
    def __str__(self)->str:
        return f"{self.idno},{super().__str__()},{self.position}"
        
    def __eq__(other:object)->bool:
        if isinstance(other,Employee):
            return other.idno == self.idno
    @abstractmethod
    def computeSalary(self)->float:
        raise NotImplementedError