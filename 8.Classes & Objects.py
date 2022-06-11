#Classes & Objects
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)
  #modify object
p1.age = 40
print(p1.age)
#40

  #delete object
del p1.name
#error!