#!/usr/bin/node
const arg1 = process.argv[2];
if (isNaN(arg1) === false) {
  for (let i = 0; i < arg1; i++) {
    console.log('C is fun');
  }
} else {
  console.log('Missing number of occurrences');
}
