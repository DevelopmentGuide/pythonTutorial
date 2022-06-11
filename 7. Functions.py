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