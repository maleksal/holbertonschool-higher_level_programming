#!/usr/bin/node
let count = 0;
process.argv.forEach((val, index) => {
  if (index === 2) {
    console.log(val);
  }
  count++;
});
if (count === 2) {
  console.log('No argument');
}
