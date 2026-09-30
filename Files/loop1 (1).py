"""
A program that would display values from 20 to 1
python loops
----------------
1. while <--classic
2. for
3. list comprehension
"""
from os import system
def main()->None:
    system("cls")
    i:int = 20              #iterator
    while i>0:              #loop condition
        print(i,end=" ")    #loop process, to be repeated
        i-=1                #loop iteration
        
if __name__=="__main__":
    main()