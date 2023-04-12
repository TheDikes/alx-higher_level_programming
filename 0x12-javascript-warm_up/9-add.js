#!/usr/bin/node
//Prints the addition of two integers

const arg1 = process.argv[2];
const arg2 = process.argv[3];

function add(a, b) {
  sum = a + b;
  return(sum);
}

add(Number(arg1), Number(arg2));
