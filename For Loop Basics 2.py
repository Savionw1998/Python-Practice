# Biggie Size - Given a list, write a function that changes all positive numbers in the list to "big".
# Example: biggie_size([-1, 3, 5, -5]) returns that same list, but whose values are now [-1, "big", "big", -5]

x = [-1,-2,-3,4,5,6,7]
def Biggie(x):
    for i in range (0, len(x)):
        if x[i] > 0:
            x[i] = "Big"
    return x
y = Biggie(x)
print (y)
# done

# Count Positives - Given a list of numbers, create a function to replace the last value with the number of positive values. (Note that zero is not considered to be a positive number).
# Example: count_positives([-1,1,1,1]) changes the original list to [-1,1,1,3] and returns it
# Example: count_positives([1,6,-4,-2,-7,-2]) changes the list to [1,6,-4,-2,-7,2] and returns it

x = [1,6,-4,-2,-7,-2]
def count_positives(x):
    sum = 0
    # newlist = []
    # L = len(x)
    for i in range (0, len(x)):
        if x[i] > 0:
            sum += 1
            while i == len(x):
                print(i)
                x[i] = sum
    return x

y = count_positives(x)
print(y)

# Sum Total - Create a function that takes a list and returns the sum of all the values in the list.
# Example: sum_total([1,2,3,4]) should return 10
# Example: sum_total([6,3,-2]) should return 7

x = [1,2,3,4,5]
def Sum_Total(x):
    sum = 0
    for i in range (x[0], len(x)):
            # print(i)
            sum += x[i]
    return i
y = Sum_Total(x)
print(y)
# Needs to grab first value

# Average - Create a function that takes a list and returns the average of all the values.x
# Example: average([1,2,3,4]) should return 2.5

x = [1,2,-3,4,5]
def Average(x):
    sum = 0
    average = 0
    for i in range (x[0], len(x)):
            sum += x[i]
            average = sum / len(x)
    return average

y = Average(x)
print(y)
# done

# Length - Create a function that takes a list and returns the length of the list.
# Example: length([37,2,1,-9]) should return 4
# Example: length([]) should return 0

x = [1,2,3,4]
def List_Length(x):
    L = len(x)
    return L
y = List_Length(x)
print(y)
# done

# Minimum - Create a function that takes a list of numbers and returns the minimum value in the list. If the list is empty, have the function return False.
# Example: minimum([]) should return -9
# Example: minimum([]) should return False

x = [37,2,1,-9,7]
def Minimum(x):
    lowest = 0
    for i in range (0, len(x)):
        if lowest > x[i]:
            lowest = x[i]
    return lowest
y = Minimum(x)
print(y)
# done

# Maximum - Create a function that takes a list and returns the maximum value in the list. If the list is empty, have the function return False.
# Example: maximum([37,2,1,-9]) should return 37
# Example: maximum([]) should return False

x = [37,2,1,-9,7,42]
def Maximum(x):
    Highest = 0
    for i in range (0, len(x)):
        if Highest < x[i]:
            Highest = x[i]
    return Highest
y = Maximum(x)
print(y)
# done

# Ultimate Analysis - Create a function that takes a list and returns a dictionary that has the sumTotal, average, minimum, maximum and length of the list.
# Example: ultimate_analysis([37,2,1,-9]) should return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 'maximum': 37, 'length': 4 }

x = [37,2,1,-9]
def Analysis(x):
    Sum = 0
    Average = Sum / len(x)
    Maximum = 0
    Minimum = 0
    for i in range (0, len(x)):
        Sum += x[i]
        Dict = {
            'average': Average,
            'maximum': Maximum,
            'minimum': Minimum,
        }
        if Minimum > x[i]:
            print (Minimum)
            Minimum = x[i]
        elif Maximum < x[i]:
            Maximum = x[i]
    return Dict
y = Analysis(x)
print(y)

# Reverse List - Create a function that takes a list and return that list with values reversed. Do this without creating a second list. (This challenge is known to appear during basic technical interviews.)
# Example: reverse_list([37,2,1,-9]) should return [-9,1,2,37]

x = [37,2,1,-9]
def Reverse(x):
        x.Reverse()
        return x
y = Reverse(x)
print(y)
