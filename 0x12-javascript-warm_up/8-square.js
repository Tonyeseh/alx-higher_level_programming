#!/usr/bin/node

const printMessage = parseInt(process.argv[2]);
if (isNaN(printMessage)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < printMessage; i++) {
    let message = '';
    for (let j = 0; j < printMessage; j++) {
      message = message + 'X';
    }
    console.log(message);
  }
}
