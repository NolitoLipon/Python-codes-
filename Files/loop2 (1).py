"""
A program that would display EVEN values from 20 to 1 python loops
----------------
1. while
2. for
3. list comprehension
"""
from os import system
def main()->None:
    system("cls")
    # for i in range(21,0,-1):  #FOR LOOP STRUCTURE
        # if i%2==0:            #data validation
            # print(i,end=" ")  #CORE LOOP PROCESS
    #list comprehension
    [print(i,end=" ") for i in range(21,0,-1) if i%2>0]
        
if __name__=="__main__":
    main()