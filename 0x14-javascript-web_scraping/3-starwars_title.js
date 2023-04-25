#!/usr/bin/node
// This script prints the title of a Star Wars movie
// where the episode number matches a given integer

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    const jsBody = JSON.parse(body);
    console.log(jsBody.title);
  }
});
