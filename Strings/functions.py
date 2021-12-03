def test():
    print("test")


def calculate(arr):
    list_num = arr.split(" ")
    num1 = float(list_num[0])
    num2 = float(list_num[2])
    if list_num[1] == '+':
        return num1 + num2
    elif list_num[1] == '-':
        return num1 - num2
    elif list_num[1] == '/':
        return num1 / num2
    elif list_num[1] == '*':
        return num1 * num2
    else:
        print("operation not available for the moment")
        return 0


def ex1(num1, num2):
    check = num1 * num2
    if check > 1000:
        return check
    else:
        return num1 + num2


def remove_chars(word, n):
    print('Original string:', word)
    x = word[n:]
    return x


def divisible_5(nums):
    for i in nums:
        if i % 5 == 0:
            print(i, end=" ")


def print_pattern(num):
    for i in range(num + 1):
        for j in range(i):
            print(i, end=" ")
        print('')


def check_palindrome(arr):
    size = len(arr) - 1
    # loop size/ 2
    for i in range(int(size / 2)):
        if arr[i] != arr[size - i]:
            print("string is palindrome")
            return None
    print("string is not palindrome")


def mearg_odd_even_list(list1, list2):
    list3 = []
    for i in list1:
        if i % 2 == 1:
            list3.append(i)
    for i in list2:
        if i % 2 == 0:
            list3.append(i)
    return list3


def reverse_order(num):
    list_reverse = []
    while num > 0:
        list_reverse.append(num % 10)
        num = int(num / 10)
    print(list_reverse)
