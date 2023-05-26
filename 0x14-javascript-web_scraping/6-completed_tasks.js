#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, (err, response, body) => {
  if (err) {
    console.error(err);
  }
  const data = JSON.parse(body);
  const tasks = {};
  for (const x in data) {
    if (data[x].completed) {
      if (!tasks[data[x].userId]) {
        tasks[data[x].userId] = 1;
      } else {
        tasks[data[x].userId]++;
      }
    }
  }
  console.log(tasks);
});
