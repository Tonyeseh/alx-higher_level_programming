#!/usr/bin/node

const firstInput = parseInt(process.argv[2]);
if (isNaN(firstInput)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + firstInput);
}
