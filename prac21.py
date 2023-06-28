#Encapsulation->methods and variables within the bounds of a given class
class Alpha:

 def __init__(self):
    self._a = 2.  # Protected member ‘a’->single underscore(_)
    self.__b = 2.  # Private member ‘b’ -> double underscore(__)