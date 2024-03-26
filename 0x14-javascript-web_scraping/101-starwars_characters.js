#!/usr/bin/node

const Api = 'http://swapi.dev/api/films/' + process.argv[2];
const request = require('request');

request(Api, function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    body = JSON.parse(body);
    const characters = body.characters;
    let count = 0;

    function getCharacterName (index) {
      if (index < characters.length) {
        request(characters[index], function (err, res, body) {
          if (err) {
            console.log(err);
          } else if (res.statusCode === 200) {
            console.log(JSON.parse(body).name);
            count++;
            getCharacterName(count);
          }
        });
      }
    }

    getCharacterName(0);
  } else {
    console.log('Error Code:' + res.statusCode);
  }
});
