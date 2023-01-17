#!/usr/bin/node

const fs = require('fs');
const request = require('request');

request(process.argv[2], (err, body) => {
  if (err) console.log(err);
  else {
    fs.writeFile(process.argv[3], body.body, (err) => {
      if (err) console.log(err);
    });
  }
});
