ii/usr/bin/node
// code checks if argument passed is a number and prints it else, prints not a number.

const arg = process.argv;
const num = +(arg[2]);

if (isNaN(num)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${num}`);
}
