#!/usr/bin/node

const request = require('request');
request.get(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  else {
    console.log('code:', response.statusCode);
  }
});
