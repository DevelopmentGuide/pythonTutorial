# Variables
# Assign1
x = "Orange"; y = z = "Banana"
print(x)
print(y)
print(z)
#Orange
#Banana
#Banana

# Assign2
x = 5; y = "John"
print(type(x))
#<class 'int'>
print(y, "is", x)
#John is 5

# Assign3
def myfunc():
  print("Name is " + y)
myfunc()
#Name is John



# Numbers
# Random
import random
print(random.randrange(1, 10))
#1 to 10
x = int(2.8) # y will be 2
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
print ("x:", x, " y:", y, " z:", z)
#x: 2  y: 2.8  z: 3.0



# String
# Multiline 
x = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(x)

# Basic Print
x = "Hello, Python!"
print(x[1])
#e
print(x[2:5])
#llo

# Each word on new Line
for x in "banana":
  print(x)
#b
#a
#n
#a
#n
#a

# Advanced output
x = "Hello, World!"
print(len(x))
#13
print(x.upper())
#HELLO, WORLD!
y = x + x
print(y)
#Hello, World!Hello, World!

txt = "The best things in life are free!"
print("free" in txt)
#True
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")
#No, 'expensive' is NOT present.

# Multi variable
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
#I want 3 pieces of item 567 for 49.95 dollars.

x = """\'1  \\2  \n3  \t4"""
print(x)
#'1  \2
#3       4



# List, Tuple & Set
thislist = ["apple", "banana"]

#basic print
print(thislist[-1])
#banana
print(thislist[0:2])
#['apple', 'banana']
print(thislist[0:])
#['apple', 'banana']

#add
thislist.insert(9, "watermelon")
print(thislist)
#['apple', 'banana', 'watermelon']
thislist.append("cherry")
print(thislist)
#['apple', 'banana', 'watermelon', 'cherry']

#extend
tropical = ["pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
#['apple', 'banana', 'watermelon', 'cherry', 'pineapple', 'papaya']

#remove
thislist.remove("banana")
print(thislist)
#['apple', 'watermelon', 'cherry', 'pineapple', 'papaya']      
thislist.clear()
print(thislist)
#[]

#more
thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)
#apple
#banana
#cherry
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#apple
#banana
#cherry

#sort
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
#[100, 82, 65, 50, 23]

#copy list
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

  #join list
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
#['a', 'b', 'c', 1, 2, 3]


# Tuples(Cant be changed)
thistuple = ("apple", "banana", "cherry")
print(thistuple)
#('apple', 'banana', 'cherry')
print(len(thistuple))
#3
print(thistuple[1])
#banana

  #remove
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

  #multiply tuple
fruits = ("apple")
mytuple = fruits * 2
print(mytuple)
#appleapple

  #intersection
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
#{'apple'}



# Dictionary
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
  #forced change
thisdict["year"] = 2018

  #update
thisdict.update({"color": "red"})

  #pop-delete
thisdict.pop("model")

print(thisdict)
#{'brand': 'Ford', 'year': 2018, 'color': 'red'}

print(thisdict["brand"])
#Ford

print(len(thisdict))
#3



#LOOP
  #IF-Else
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
#a is greater than b


  #While
i = 4
while i < 6:
  print(i)
  i += 1
#4
#5

  #continue
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
#apple
#cherry

  #range
for x in range(2):
  print(x)
#0
#1

  #nested Loop
x = ["1", "2", "3"]
y = ["4", "5", "6"]
for a in x:
  for b in y:
    print(a,b)



#Functions
def my_function(fname, lname):
  print(fname + "-" + lname)

my_function("Emil", "Refsnes")
#Emil-Refsnes

def my_function(c1,c2,c3):
  print("Lowest number is-" + c1)
  print("followed by-" + c2 + c3)
my_function(c1="2", c2="3", c3="5")
#Lowest number is-2
#followed by-35

  #lambda
x = lambda a : a + 10
print(x(5))
#15

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
#22



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




#Inheritance
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()