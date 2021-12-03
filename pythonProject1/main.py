# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# settingsfrom platform import python_version
# print("testing one two three")
#
# print(python_version())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
# a = 3.5
# b = int(a)
#
# print(type(b))
# unpack multi values mus tbe equal or else error
# fruits = ["apple", "banana", "3dfgs", "cherry"]
# x, y, z , t = fruits
# print(fruits[2])
# print(x)
# print(y)
# print(z)

# a = 4
# x = "awesome"
# # use str() or down below
# print("Python is " + x + " ", a, "sdfsdf")

# txt = "The best things in life are free!"
# print("free" in txt)
#
# txt = "The best things in life are free!"
# print("expensive" not in txt)

# slice string
# b = "                 Hello, World!                             0 "
# print(b[-3])
#
# print(b[-5:-2])

# print(b.strip())

# placeholder for numbers it can hold ultimate number of values
# quantity = 3
# itemno = 567
# price = 49.95
# myorder = "I want {} pieces of item {} for {} dollars."
# print(myorder.format(quantity, itemno, price))
#
# a = "Hello, World! this is messed up, maybe new list"
# b = a.split(" ")
# print(b)
# print(b[1])
#
# for x in range(5):
#     print(b[x])
# rt = "hello"
# print(type(rt))


thisdict =	{
  "brand": ["Ford", "honda", "toyota"],
  "model": "Mustang",
  "year": [1964, 200]
}
print(thisdict.get("model"))
print("======================")
# thisdict["brand"] = "yamaha"
# x = thisdict.values()
#
# print(thisdict["brand"]) #before the change
for x in thisdict:
  print(thisdict[x])
# print(thisdict.items())

print("==========================")
#
# if "year" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")