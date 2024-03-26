#!/usr/bin/node

const Api = 'http://swapi.dev/api/films/' + process.argv[2];
const request = require('request');

request(Api, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    body = JSON.parse(body);
    for (const char in body.characters) {
      request(body.characters[char], function (err, res, body) {
        if (err) {
          console.log(err);
        } else if (res.statusCode === 200) {
          console.log(JSON.parse(body).name);
        }
      });
    }
  } else {
    console.log('Erorr Code:' + res.statusCode);
  }
});
