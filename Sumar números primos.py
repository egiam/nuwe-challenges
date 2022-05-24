# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

sum = 0
primes = []
Stop = False

for x in range(2, 2000000):
    Stop = False

    if x == 2:
        sum+=x
        primes.append(x)
        continue

    for i in range(len(primes)):
        if x % primes[i] == 0:
            Stop = True
            break
    
    if Stop:
        continue

    sum+=x
    primes.append(x)

print(f"Total: {sum} - Array: {primes}")
