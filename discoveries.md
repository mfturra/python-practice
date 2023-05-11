# Git Commands
git branch --show-current



# Classes & Methods
### Functions
@classmethod or classmethod()
- Definition: Returns a class method for a specific function. Completely contingent on being used inside/with a function and is bound to a class rather than an object.
Example
```
@classmethod
def function(cls, argument, ...)
```

Definition Continued
- Takes a single parameter, a function, whose output needs to be converted into a class.
- Requires the first argument being the class itself ```cls```. 
Example
```
def classMethod(cls, args...)
```

How does instantiation work?

## __str__() and __repr__()
__str__(): Returns a human-readable, or informal, string representation of an object. Customarily called by print(), str(), and format() functions. When __str__() isn't the method defined for the class, then object implementation will call the __repr__() method.

__repr__(): Returns a more information-rich, or official, string representation of an object. Called by the repr() function. In all cases, the string should be informative and unambiguous. 

Generally speaking __str__() is intended for users and __repr__() is intended for developers. 

- When creating a class, the __repr__() method should be used so that useful information is returned when built-in functions use it.
- __str__ and __repr__ is required if the developer wants to print information about a class. If neither are implemented then the output becomes the object id in a hexadecimal format.

## The use of *args and **kwargs
*args and **kwargs are arguments passed into functions
- Where *args is an argument wrapped up in a tuple (single variable with multiple values)