#!/usr/bin/node

const printMessage = parseInt(process.argv[2]);
if (isNaN(printMessage)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < printMessage; i++) {
    console.log('C is fun');
  }
}
