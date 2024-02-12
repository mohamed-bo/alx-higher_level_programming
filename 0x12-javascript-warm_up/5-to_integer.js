#!/usr/bin/node
const agruments = process.argv.slice(2);

if (isNaN(agruments[0])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(agruments[0]));
}
