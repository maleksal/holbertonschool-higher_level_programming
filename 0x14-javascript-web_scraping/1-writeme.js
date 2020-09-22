#!/usr/bin/node
const fs = require('fs');
const contentFile = process.argv[2];
const toWrite = process.argv[3];

fs.readFile(contentFile, 'utf-8', (error, text) => {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(toWrite, text, 'utf-8', (err) => {
      if (err) { console.log(err); }
    });
    console.log(text);
  }
});
