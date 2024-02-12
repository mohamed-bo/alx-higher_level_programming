#!/usr/bin/node

const myVar = 'C is fun';
const numer = parseInt(process.argv[2]);

if (isNaN(numer)) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < numer; i++) {
    console.log(myVar);
  }
}