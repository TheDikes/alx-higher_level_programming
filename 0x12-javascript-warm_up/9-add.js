#!/usr/bin/node
const arg1 = process.arg[2];
const arg2 = process.arg[3];

function add(a, b) {
  console.log(a + b);
}

add(Number(arg1), Number(arg2));
