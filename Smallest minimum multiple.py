# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

number = 2520;
condition = 0;
while condition < 20:
    condition = 0;
    for x in range(1,21):
        if (number % x == 0):
            condition += 1;
    if condition >= 20:
        print(number)
    number += 20;
