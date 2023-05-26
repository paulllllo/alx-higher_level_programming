#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    return console.error(error);
  }
  let count = 0;
  const results = JSON.parse(body).results;
  for (const x in results) {
    for (const character in results[x].characters) {
      if (results[x].characters[character] === 'https://swapi-api.alx-tools.com/api/people/18/') {
        count++;
      }
    }
  }
  console.log(count);
});
