#!/usr/bin/node
// This code prints the second biggest number in the lists of arguments.

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const num = process.argv.slice(2);
  const sortedNum = num.sort((a, b) => b - a);
  console.log(sortedNum[sortedNum[1]);
}
