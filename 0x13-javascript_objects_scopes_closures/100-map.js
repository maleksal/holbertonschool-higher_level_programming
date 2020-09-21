#!/usr/bin/node
const list = module.require('./test.js').list;
console.log(list);
console.log(list.map(i => i * list.indexOf(i)));
