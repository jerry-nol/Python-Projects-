from abc import ABC, abstractmethod

#parent class
class Animal(ABC):
    def move(self):
        pass

#Child class #1
class Human(Animal):
    #Overriding abstract method
    def move(self):
        print("I can walk and talk")

#Child class #2
class Lion(Animal):
    def move(self):
        print("I roar")

#using a different name for functions

H = Human()
H.move() #calling the move function from the Human class

L = Lion()
L.move() #calling the move function from the Lion class
