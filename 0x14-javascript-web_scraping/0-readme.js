#!/usr/bin/node
// A script created to print the content of a file

let fs = require('fs');
const filePath = process.argv[2];
fs.readFile(filePath, 'utf8', (err, data) => {
    if (err) {
        console.log(err);
    }
    else {
        console.log(data);
    }
})
