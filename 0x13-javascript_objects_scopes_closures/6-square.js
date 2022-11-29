#!/usr/bin/node
const Rectangle = require('./4-rectangle');

module.exports = class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      let string;
      for (let i = 0; i < this.height; i++) {
        string = '';
        for (let j = 0; j < this.width; j++) { string = string + c; }
        console.log(string);
      }
    }
  }
};
