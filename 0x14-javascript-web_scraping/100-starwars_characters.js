#!/usr/bin/node

const request = require('request');

const filmUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(filmUrl, (err, response, body) => {
  if (!err) {
    const charUrl = JSON.parse(body).characters;
    for (const url of charUrl) {
      request(url, (err, response, body) => {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
