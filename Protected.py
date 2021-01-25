

class Protected:
    def __init__(self):
        self.__privateVar = 24

    def getPrivate(self): #funtion that prints privateVar variable
        print(self.__privateVar)

    def setPrivate(self,private):
        self.__privateVar = private #Storing self.__privateVar in private variable


obj = Protected()
obj.getPrivate() # calling the getPrivate function
obj.setPrivate(56) #Setting a new value to private variable
obj.getPrivate() #Calling getPrivate once again to see new set value

class Protected:
    def __intit__(self):
        self._protectedVar = 5 

obj = Protected() #storing protected function in obj variable  
obj._protectedVar = 10 #Changing the value of _protectedVar
print(obj._protectedVar) #print the result
