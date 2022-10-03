#!/usr/bin/node

const x = parseInt(process.argv[2], 10);
const y = parseInt(process.argv[3], 10);
function add (a, b) {
  return (a + b);
}
console.log(add(x, y));
