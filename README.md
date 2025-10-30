# OPPS-PYTHON
Class Work and Assignments Section 2

1. What is polymorphism?

Polymorphism means “many forms”. In the context of object-oriented programming, it refers to the ability of the same interface (method name/operator) to behave differently depending on the object it is working with.

In Python the key types of polymorphism discussed are:
-Method overriding (runtime polymorphism) – where a subclass replaces a parent class method.
-Using the same operator (or function) for different types (e.g., + working on ints, strings, lists) – also called operator overloading in other languages, though Python handles it dynamically.
-Duck-typing / functions that accept different kinds of objects as long as they support the required method.

2. The __class__.__name__ bit

-in a “print section” using something like A.__class__.__name__ (or self.__class__.__name__). What that does is:

-obj.__class__ gives you the class (type) of the object obj.

-obj.__class__.__name__ gives the name of that class as a string. For example, if you have class Dog: and d = Dog(), then d.__class__.__name__ is "Dog".
-It’s typically used in print/statements to dynamically display “which class” this object belongs to (especially in polymorphism examples, where you might have mixed objects and you want to print something like “Dog goes Bark” or “Cat goes Meow” using the class name).
print(f"{obj.__class__.__name__} says {obj.sound()}")

-It means: for any object obj, print its class’s name and then call its sound() method. This helps illustrate that polymorphism is at work: different objects, same method name sound(), different outputs.
