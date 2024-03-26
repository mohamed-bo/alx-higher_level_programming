#!/usr/bin/node
const request = require('request');
const api = 'http://swapi.co/api/films/' + process.argv[2];

request(api, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    body = JSON.parse(body);
    console.log(body.title);
  } else {
    console.log('Erorr Code:' + res.statusCode);
  }
});
