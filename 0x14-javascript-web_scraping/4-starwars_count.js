#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (_error, _res, body) {
  const bodyParsed = JSON.parse(body).results;
  let occurenceNumber = 0;
  for (let i = 0; i < bodyParsed.length; ++i) {
    const chrcts = bodyParsed[i].characters;

    for (let j = 0; j < chrcts.length; ++j) {
      const character = chrcts[j];
      const characterId = character.split('/')[5];

      if (characterId === '18') {
        occurenceNumber += 1;
      }
    }
  }
  console.log(occurenceNumber);
});
