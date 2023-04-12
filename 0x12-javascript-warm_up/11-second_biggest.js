#!/usr/bin/node
// This code prints the second largest number among the arguments passed to it.

if (!process.argv[2] || !process.argv[3]) {
  console.log(0);
} else {
  const numbers = process.argv.slice(2);
  const sortedNumbers = numbers.sort((a, b) => a - b);
  console.log(sortedNumbers[sortedNumbers.length - 2]);
}
