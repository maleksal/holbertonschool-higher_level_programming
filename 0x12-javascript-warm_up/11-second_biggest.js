#!/usr/bin/node
const arr = [];

process.argv.forEach((val, index) => {
  if (isNaN(val) === false) {
    arr.push(parseInt(val));
  }
});

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const maxval = Math.max.apply(null, arr);
  arr.splice(arr.indexOf(maxval), 1);
  console.log(Math.max.apply(null, arr));
}
