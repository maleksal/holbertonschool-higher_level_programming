#!/usr/bin/node
const arg1 = process.argv[2];
if (isNaN(arg1) === false) {
  console.log(`My number: ${arg1}`);
} else {
  console.log('Not a number');
}
