'''
	Person class
'''
class Person(object):
    #class constructor
    def __init__(self,lastname:str,firstname:str)->None:   
        self.lastname = lastname
        self.firstname = firstname
        
    def __str__(self)->str:
        return f"{self.lastname},{self.firstname}"
    
    def __eq__(other:object)->bool:
        if isinstance(other,Person):
            return other.lastname == self.lastname and other.firstname== self.firstname
                
    
        