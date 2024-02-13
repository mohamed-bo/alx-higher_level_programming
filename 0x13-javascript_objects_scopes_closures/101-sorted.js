#!/usr/bin/node

const dict = require('./101-data').dict;

const occurece = {};

for (const key in dict) {
  if (occurece[dict[key]] === undefined) {
    occurece[dict[key]] = [];
  }
  occurece[dict[key]].push(key);
}

console.log(occurece);
