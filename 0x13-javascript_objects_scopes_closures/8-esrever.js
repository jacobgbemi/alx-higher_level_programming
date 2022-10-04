#!/usr/bin/node

exports.esrever = function (list) {
  const newList = [];
  let first = 0;
  const last = list.length - 1;
  for (first = 0; first < list.length; first++) {
    newList.push(list[last - first]);
  }
  return newList;
};
