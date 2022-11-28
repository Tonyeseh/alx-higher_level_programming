#!/usr/bin/node

first_input = parseInt(process.argv[2]);
if (isNaN(first_input)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + first_input);
}
