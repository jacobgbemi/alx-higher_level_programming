#!/usr/bin/node

let count = -1;
exports.logMe = function (item) {
  count++;
  console.log(count + ': ' + item);
};
