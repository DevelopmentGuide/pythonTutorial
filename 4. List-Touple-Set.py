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