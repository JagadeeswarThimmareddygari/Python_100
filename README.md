# Object Oriented Programming Fundamentals
Programmers would have heard the word "object oriented programming", and some people often ask if they can explain "object oriented programming" is in one sentence. Let's take a look at the formal statement first.

*"Compose a set of  data structures and methods to process them into objects, group objects with same behaviour into the classes, hide internal details through the encapsulation, and realize class specilization through inheritance, and generalization through polymorphism to achieve dynamic assignment based on object type.*

##Classes and Objects

Class is a blue print and template of an object, and an object is an instance of the class. 
Classes are abstract concept and objects are concrete things.
Objects have attributes and behaviours. Each object is unique and must belong to a certain class(type). When we extract static characteristics(attributes) and dynamic characteristics(behaviors) of large number of objects with common characteristics, we define something called a "Class".

![objects](https://github.com/jackfrued/Python-100-Days/raw/master/Day01-15/res/object-feature.png)

## Definition of class

In python, you can use class keyword to define a class, and define methods in the class.

```python
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    
    def study(self,course_name):
        print('%s is learning %s' %(self.name,course_name))
    
    def watchmovie(self):
        if self.age<18:
            print('%s can only watch pokemon'%(self.name))
        else:
            print("%s is watching the island country movie."%(self.name))
 ```

 ## Create and use objects
 
 After we define a class, we can create an object and send a message to the object in the following way.
 
 ```python
 stu1=Student('jd',20)
stu1.study('python')
stu1.watchmovie()

stu2=Student("novin",22)
stu2.study("AWS")
stu2.watchmovie()
```
## Public Members

Public members (generally methods declared in a class) are accessible from outside the class. The object of the same class is required to invoke a public method. This arrangement of private instance variables and public methods ensures the principle of data encapsulation.

All members in a Python class are public by default. Any member can be accessed from outside the class environment.

```python
class Student:
    schoolName = 'XYZ School' # class attribute

    def __init__(self, name, age):
        self.name=name # instance attribute
        self.age=age # instance attribute
    
std = Student("Steve", 25)
print(std.schoolName)  #'XYZ School'
std.age=20
print(std.age) # 20
```

## Protected Members

Protected members of a class are accessible from within the class and are also available to its sub-classes. No other environment is permitted access to it. This enables specific resources of the parent class to be inherited by the child class.

Python's convention to make an instance variable protected is to add a prefix _ (single underscore) to it. This effectively prevents it from being accessed unless it is from within a sub-class.

```python
class Student:
    _schoolName = 'XYZ School' # protected class attribute
    
    def __init__(self, name, age):
        self._name=name  # protected instance attribute
        self._age=age # protected instance attribute
std = Student("Swati")
print(std.name) # Swati
```
>Note: However, it is still accessible in Python. Hence, the responsible programmer would refrain from accessing and modifying instance variables prefixed with _ from outside its class.

## Private Members

Python doesn't have any mechanism that effectively restricts access to any instance variable or method. Python prescribes a convention of prefixing the name of the variable/method with a single or double underscore to emulate the behavior of protected and private access specifiers.

The double underscore __ prefixed to a variable makes it private. It gives a strong suggestion not to touch it from outside the class. Any attempt to do so will result in an AttributeError.

```python
class Student:
    __schoolName = 'XYZ School' # private class attribute

    def __init__(self, name, age):
        self.__name=name  # private instance attribute
        self.__salary=age # private instance attribute
    def __display(self):  # private method
	    print('This is private method.')
std = Student("Bill", 25)
print(std.__schoolName)
#AttributeError: 'Student' object has no attribute '__schoolName'
print(std.__name(
#AttributeError: 'Student' object has no attribute '__name'
print(std.__display())
#AttributeError: 'Student' object has no attribute '__display'
```
Python performs name mangling of private variables. Every member with a double underscore will be changed to _object._class__variable. So, it can still be accessed from outside the class, but the practice should be refrained.

```python
std = Student("Bill", 25)
print(std._Student__name)
#'Bill'
std._Student__name = 'Steve'
print(std._Student__name)
#'Steve'
print(std._Student__display())
#'This is private method.'
```
 ## Exercise
 
 Exercise1: Define a class to describe digital clocks.
 
 ### Reference Answer:
 
 '''python
 # -*- coding: utf-8 -*-
"""
Created on Tue May 25 16:10:24 2021

@author: Jagadeeswar190
"""

from time import sleep


class Clock:
    def __init__(self,hour,minute,second):
        self._hour=hour
        self._minute=minute
        self._second=second
    
    def run(self):
        self._second+=1
        if self._second==60:
            self._second=0
            self._minute+=1

            if self._minute==60:
                self._minute=0
                self._hour+=1
        
                if self._hour==24:
                    self._hour=0
    
    def display(self):
        """Displaying time"""
        return  '%02d:%02d:%02d'  % ( self . _hour , self . _minute , self . _second )
        #print("{0}:{1}:{2}".format(self._hour,self._minute,self._second))

def main():
    clock=Clock(23,59,58)
    while True:
        print(clock.display())
        sleep(1)
        clock.run()

if __name__ =='__main__':
    main()
```
