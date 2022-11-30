#!/usr/bin/node

const fs = require('fs');

file1 = fs.readFileSync(process.argv[2], 'utf8');
file2 = fs.readFileSync(process.argv[3], 'utf-8');

fs.writeFileSync(process.argv[4], file1 + file2);
