import random
def randInt(min=int(), max= int()):
    if max <= 50:
        num = random.random() * 50
    elif min >= 50:
        num = random.random() * 100 - 50
    else:
        num = random.random() * 100
    return num


print(randInt()) 		    # should print a random integer between 0 to 100
print(randInt(max=50)) 	    # should print a random integer between 0 to 50
print(randInt(min=50)) 	    # should print a random integer between 50 to 100
print(randInt(min=50, max=500))    # should print a random integer between 50 and 500