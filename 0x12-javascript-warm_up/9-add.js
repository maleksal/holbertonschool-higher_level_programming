#!/usr/bin/node
const number1 = process.argv[2];
const number2 = process.argv[3];

function add (n1, n2) {
  if (isNaN(n1) || isNaN(n2)) {
    return (NaN);
  } else {
    return (parseInt(n1) + parseInt(n2));
  }
}
console.log(add(number1, number2));
