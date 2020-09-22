#!/usr/bin/node
const request = require('request');
const baseUrl = process.argv[2];
let output = [];
request.get(baseUrl, (error, respponse, body) => {
  if (error) {
    console.log(error);
  } else {
    output = JSON.parse(body).results;
    let count = 0;
    for (let i = 0; i < output.length; i++) {
      const characters = output[i].characters;
      for (let e = 0; e < characters.length; e++) {
        if (characters[e].endsWith('/18/')) {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
