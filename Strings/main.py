import functions
import random
from functions import test

# num = input("Enter the equation :")
# print(functions.calculate(num))

print(functions.ex1(30, 20))
a = "1234567890"
print(functions.remove_chars(a, 4))
nums = [10, 20, 22, 33, 30, 35, 40]
print("Nums divided by 5")
functions.divisible_5(nums)


functions.print_pattern(5)

arr = '10011'
print("================")
functions.check_palindrome(arr)
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

print(functions.mearg_odd_even_list(list1, list2))

functions.reverse_order(7536)
