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
