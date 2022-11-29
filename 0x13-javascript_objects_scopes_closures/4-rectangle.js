#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let string = '';
      for (let j = 0; j < this.width; j++) {
        string = string + 'X';
      }
      console.log(string);
    }
  }

  rotate () {
    for (let i = 0; i < this.width; i++) {
      let string = '';
      for (let j = 0; j < this.height; j++) {
        string = string + 'X';
      }
      console.log(string);
    }
  }

  double () {
    for (let i = 0; i < this.height * 2; i++) {
      let string = '';
      for (let j = 0; j < this.width * 2; j++) {
        string = string + 'X';
      }
      console.log(string);
    }
  }
};
