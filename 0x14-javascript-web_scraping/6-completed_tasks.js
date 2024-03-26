#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, res, body) {
  if (error) {
    console.log(error);
  } else {
    const cmpltedTask = {};

    const bodyParsed = JSON.parse(body);
    for (let i = 0; i < bodyParsed.length; ++i) {
      const uid = bodyParsed[i].uid;
      const finished = bodyParsed[i].completed;

      if (finished && !cmpltedTask[uid]) {
        cmpltedTask[uid] = 0;
      }
      if (finished) {
        cmpltedTask[uid]++;
      }
    }
    console.log(cmpltedTask);
  }
});
