i#!/usr/bin/node
function factorial(num) {
  if (num < 2 || isNaN(num) {
    return(1);
  }
  return(num * factorial(num - 1));
}

console.log(factorial(process.argv[2]));
