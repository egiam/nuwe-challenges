// The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

// Find the sum of all the primes below two million.

let sum = 0;
let primes = [];
let Stop = false;

for (let x = 2; x < 2000000; x++) {
    Stop = false;

    if (x === 2) {
        sum += x;
        primes.push(x);
        continue;
    }

    for (let i = 0; i < primes.length; i++) {
        if (x % primes[i] === 0) {
            Stop = true;
        }
    }

    if (Stop) {
        continue;
    }

    sum += x;
    primes.push(x);
}

console.log(`Total: ${sum} - Array: ${primes}`);