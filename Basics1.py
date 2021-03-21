for x in range(51):
    print(x)

for x in range(5, 1000, 5):
    print(x)

for x in range(101):
    # print(f"Mod {x % 5}")
    if x % 10 == 0:
        print("coding dojo")
    elif x % 5 == 0:
        print("coding")
    else:
        print(x)

for x in range(1, 20, 2):
    sum = 0
    sum += x
    print(sum)

for x in range(100, 1, -4):
    print(x)

high_num = 9
low_num = 2
Mult = 3
for x in range(2, 10, 1):
    if x % Mult == 0:
        print(x)