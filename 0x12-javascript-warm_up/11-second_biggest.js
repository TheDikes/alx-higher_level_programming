#!/usr/bin/node
// This code prints the second biggest number int the list of arguments

const args = process.argv.slice(2).map(Number);

if (args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort((a, b) => b - a);
  let secBiggest = sortedArgs[1];
  console.log(Number.isInteger(secBiggest) ? secBiggest : 0);
}
