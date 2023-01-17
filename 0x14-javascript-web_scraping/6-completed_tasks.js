#!/usr/bin/node

const request = require('request');
request(process.argv[2], (err, body) => {
  if (err) console.log(err);
  else {
    const completed = {};
    for (const todo of JSON.parse(body.body)) {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId] += 1;
        }
      }
    }
    console.log(completed);
  }
});
