#!/usr/bin/node
const arg1 = process.argv[2];
if (isNaN(arg1) === false) {
  for (let i = 0; i < arg1; i++) {
    console.log('X'.repeat(arg1));
  }
} else {
  console.log('Missing size');
}
