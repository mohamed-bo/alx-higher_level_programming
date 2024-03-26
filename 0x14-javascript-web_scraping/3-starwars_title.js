#!/usr/bin/node
const request = require('request');
const { film } = require('process');

const url = 'https://swapi-api.hbtn.io/api';
request(url + '/films/' + film[2], (error, res, body) => {
  if (error) {
    console.error(error);
  }
  console.log(JSON.parse(body).title);
});
