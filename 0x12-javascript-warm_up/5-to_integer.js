#!/usr/bin/node
// code checks if argument passed is a number and prints it else, prints not a number.

const arg = process.argv;
const number = parseInt(arg[2]);

if (isNaN(number)) {
  console.log('Not a number');
} else {
  console.log('My number: ' + number);
}
