#!/usr/bin/node
const fs = require('fs');
const contentFile = process.argv[2];
const toWrite = process.argv[3];

fs.writeFile(contentFile, toWrite, 'utf-8', (error) => {
  if (error) {
    console.log(error);
  }
});
