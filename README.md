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
