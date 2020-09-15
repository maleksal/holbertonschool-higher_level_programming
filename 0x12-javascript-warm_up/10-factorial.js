#!/usr/bin/node
const number1 = process.argv[2];

function factorial (num) {
  if (isNaN(num) || num === 0) {
    return 1;
  } else {
    return parseInt(num) * factorial(parseInt(num) - 1);
  }
}

console.log(factorial(number1));
