#!/usr/bin/node

const url = process.argv[2];
const filename = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(filename, body, 'utf8');
  }
});
