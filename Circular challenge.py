# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

# How many circular primes are there below one million?

quantity = 0;
# numero = 135
# numero = str(numero);
num = 0
posibility = False;

# for j in range(0,len(str(numero)) - 1):
#     if (j == 0):
#         num = numero[len(str(numero)) - 1]
#     num += numero[j]
#     print(num)

for x in range(2,101):
    x = str(x);
    for h in range(len(x) + 1):
        for j in range(len(x)):
            if (j == 0):
                num = x[len(x) - 1]
            else:
                num += x[j]
            print(num)
        for i in range(2, int(x)):
            if int(num) % i != 0:
                posibility = True;
            else:
                posibility = False;
    if posibility:
        quantity += 1;

print(quantity)
