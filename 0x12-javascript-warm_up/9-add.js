ii/usr/bin/node
//This script prints the addition of two integers

function add (a, b) {
  const sum = a + b;
  console.log(sum);
}

add(Number(process.argv[2]), Number(process.argv[3]));
