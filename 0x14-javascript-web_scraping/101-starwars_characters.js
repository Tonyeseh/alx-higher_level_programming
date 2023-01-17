#!/usr/bin/node

const request = require('request');

const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(filmUrl, (err, response, body) => {
  if (!err) {
    const charUrl = JSON.parse(body).characters;
    printName(charUrl, 0);
  }
});

function printName (charUrl, idx) {
  request(charUrl[idx], (err, response, body) => {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (idx + 1 < charUrl.length) {
        printName(charUrl, idx + 1);
      }
    }
  });
}
