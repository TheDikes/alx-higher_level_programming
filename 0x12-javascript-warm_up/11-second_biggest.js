#!/usr/bin/node
// This code prints the second largest number among the arguments passed to it.

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const num = process.argv.slice(2);
  const sortedNum = numb.sort((a, b) => b - a);
  console.log(sortedNum[sortedNum[1]);
}
