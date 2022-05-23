// 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

// What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

let number = 2520;
let condition = 0;
while (condition < 20) {
    condition = 0;
    for (let x = 1; x < 21; x++) {
        if (number % x === 0) condition += 1;
    }
    number += 20;
}

console.log(number);