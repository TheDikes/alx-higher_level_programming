#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0) {
      // If w or h is zero or negative, create an empty object
      return;
    }
      this.width = w;
      this.height = h;
    }
  }

module.exports = Rectangle;
