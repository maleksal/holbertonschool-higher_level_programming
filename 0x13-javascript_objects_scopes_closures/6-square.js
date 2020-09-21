#!/usr/bin/node

const _Square = module.require('./5-square.js');

class Square extends _Square {
  charPrint (c) {
    if (!c) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        console.log(`${c}`.repeat(this.height));
      }
    }
  }
}

module.exports = Square;
