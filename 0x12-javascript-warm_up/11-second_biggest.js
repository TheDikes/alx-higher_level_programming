#!/usr/bin/node
//This code prints the second biggest integer in the list of arguments

const args = process.argv.slice(2).map(Number);

if (args.length <= 1) {
  console.log(0);
} else {
  