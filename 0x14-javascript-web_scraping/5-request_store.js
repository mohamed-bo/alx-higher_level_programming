#!/usr/bin/node
const fs = require('fs');
const request = require('request');

request(process.argv[2], function (_error, _res, body) {
  fs.writeFile(process.argv[3], body, 'utf8', function (error) {
    if (error) {
      console.log(error);
    }
  });
});
