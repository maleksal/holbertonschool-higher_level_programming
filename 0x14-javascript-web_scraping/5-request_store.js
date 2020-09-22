#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const baseUrl = process.argv[2];
const file = process.argv[3];
request.get(baseUrl, (error, respponse, body) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(file, body, 'utf-8', (error) => {
      if (error) {
        console.log(error);
      }
    });
  }
});
