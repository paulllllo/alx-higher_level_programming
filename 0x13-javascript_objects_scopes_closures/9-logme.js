#!/usr/bin/node
const num = 0;
exports.logMe = function (item) {
    console.log(`${num}: ${item}`);
    num++;
}
