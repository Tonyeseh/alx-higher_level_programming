#!/usr/bin/node

let max = 0;
let secondMax = 0;
let num;

for (let i = 2; i < process.argv.length; i++) {
  num = parseInt(process.argv[i]);
  if (num > max) {
    secondMax = max;
    max = num;
  } else if (num > secondMax) {
    secondMax = num;
  }
}

console.log(secondMax);
