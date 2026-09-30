'''
	Student class
'''
from os import system
from Person import Person
class Student(Person):
    def __init__(self,idno,lastname,firstname,course,level)->None:
        super().__init__(lastname,firstname)
        self.idno=idno
        self.course=course
        self.level=level
        
    def __str__(self)->None:
        return self.idno+","+super().__str__()+","+self.course+","+self.level
        
    def __eq__(self,other:object)->bool:
        if isinstance(other,Student):
            return other.idno == self.idno
            
def main()->None:
    system('cls')
    s=Student('1000','durano','dennis','bscs','4')
    t=Student('1000','xxxx','yyy','bscs','4')
    print(s)
    print(t)
    print(f"{s} is equal to {t} {s.__eq__(t)}")
    
    
if __name__=="__main__":
    main()
    