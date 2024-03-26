#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  } else if (res.statusCode === 200) {
    const structu = {};
    const todo = JSON.parse(body);

    for (const i in todo) {
      if (todo[i].completed) {
        if (structu[todo[i].userId] === undefined) {
          structu[todo[i].userId] = 1;
        } else {
          structu[todo[i].userId]++;
        }
      }
    }
    console.log(structu);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
