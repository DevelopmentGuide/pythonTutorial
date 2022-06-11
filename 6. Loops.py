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