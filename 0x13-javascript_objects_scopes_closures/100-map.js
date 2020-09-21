#!/usr/bin/node
const list = module.require('./100-data.js').list;
console.log(list);
console.log(list.map(i => i * list.indexOf(i)));