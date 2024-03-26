#!/usr/bin/node
const request = require('request');
const api = 'http://swapi.dev/api/films/' + process.argv[2];

request(api, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log('Erorr Code:' + res.statusCode);
  }
});
