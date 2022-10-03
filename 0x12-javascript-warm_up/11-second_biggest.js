#!/usr/bin/node

function compare (a, b) {
  return b - a;
}
const arg = process.argv.length;
if (arg <= 3) {
  console.log(0);
} else {
  console.log(process.argv.slice(2).sort(compare)[1]);
}
