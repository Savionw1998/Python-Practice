# Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    newarr = []
    for i in range (num, 0, -1):
        newarr.append(num)
        print(num)
        num -= 1
    return newarr
countdown(33)

# Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
# Example: print_and_return([1,2]) should print 1 and return 2
x = [3,4]
def print_and_return(x):
    v = x[0]
    b = x[1]
    print(v)
    return(b)
y = print_and_return(x)
print(y)

# First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
# Example: first_plus_length([1,2,3,4,5]) should return 6 (first value: 1 + length: 5)
x = [1,2,3,4,5] 
def first_plus_length(x):
        return x[0] + len(x)
y = first_plus_length(x)
print (y)

# Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
# Example: values_greater_than_second([5,2,3,2,1,4]) should print 3 and return [5,3,4]
# Example: values_greater_than_second([3]) should return False

x = [1,5,3,6,9,8]
def greater_than_second(x):
    newlist = []
    sum = 0
    for i in range (x[0], len(x)):
        if x[i] > x[1]:
            newlist.append(x[i])
            sum += 1
    print(sum)
    return newlist

y = greater_than_second(x)
print(y)

# This Length, That Value - Write a function that accepts two integers as parameters: size and value. The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
# Example: length_and_value(4,7) should return [7,7,7,7]
# Example: length_and_value(6,2) should return [2,2,2,2,2,2]

x = [4,9]
def this_length(x):
    newlist = []
    newlist.append(x[1])
    return newlist*x[0]
y = this_length(x)
print(y)