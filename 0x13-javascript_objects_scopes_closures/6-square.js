#!/usr/bin/node
const Square0 = require('./5-square');

module.exports = class Square extends Square0 {

  charPrint (c) {
    if (c === undefined) {
      super.print();
    } else {
      const string = c.repeat(this.width);
      for (let i = 0; i < this.height; i++) {
        console.log(string);
      }
    }
  }
};
