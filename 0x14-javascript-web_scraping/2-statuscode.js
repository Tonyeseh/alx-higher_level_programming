#!/usr/bin/node

request = require('request');
request.get(process.argv[2], (err, response, body) => {
  console.log('code:', response.statusCode);
});
