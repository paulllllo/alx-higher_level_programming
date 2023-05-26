#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request(url, (err, response, body) => {
  if (err) {
    return console.error(err);
  }
  fs.writeFile(file, body, { encoding: 'utf8' }, (err) => {
    if (err) {
      console.error(err);
    }
  });
});
