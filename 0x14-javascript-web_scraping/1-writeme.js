#!/usr/bin/node
const fs = require('fs');
const contentFile = process.argv[2];
const toWrite = process.argv[3];

fs.writeFile(toWrite, contentFile, 'utf-8', (err) => {
  if (err) {
    console.log(err);
  }
});
