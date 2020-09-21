#!/usr/bin/node

const dictionary = module.require('./test.js').dict;
const newDic = {};

for (const key in dictionary) {
  if (newDic[dictionary[key]] !== undefined) {
    newDic[dictionary[key]].push(key);
  } else {
    newDic[dictionary[key]] = [key];
  }
}
console.log(newDic);
