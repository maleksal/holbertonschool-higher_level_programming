#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let allTodos;
const dictionary = {};
request.get(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    allTodos = JSON.parse(body);
    for (const i in allTodos) {
      if (allTodos[i].completed === true) {
        if (!dictionary[allTodos[i].userId]) {
          dictionary[allTodos[i].userId] = 1;
        } else {
          dictionary[allTodos[i].userId]++;
        }
      }
    }
  }
  console.log(dictionary);
});
