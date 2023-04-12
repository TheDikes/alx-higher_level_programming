#!/usr/bin/node
function factorial(num) {
  if (num === 0) {
    return 1;
  }
  return (num * factorial(num - 1));
}

console.log(factorial(+(process.argv[2])));
