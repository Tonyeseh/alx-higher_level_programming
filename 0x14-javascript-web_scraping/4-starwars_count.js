#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, response, body) => {
  if (err) console.log(err);
  else {
    const results = JSON.parse(body).results;
    let count = 0;
    for (const film of results) {
      for (const cha of film.characters) {
        if (cha.includes('18')) count++;
      }
    }
    console.log(count);
  }
});
