#!/usr/bin/node
const fs = require('fs');

fs.writeFileSync(process.argv[4],
  fs.readFileSync(process.argv[2], 'utf-8') + fs.readFileSync(process.argv[3], 'utf-8'));
