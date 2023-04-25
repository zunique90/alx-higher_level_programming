#!/usr/bin/node
// This script prints all characters of a Star Wars movie

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, function (err, data, body) {
  if (!err) {
    const chars = JSON.parse(body).characters;
    chars.forEach((c) => {
      request(c, function (err, data, body) {
        if (!err) {
          console.log(JSON.parse(body).name);
        }
      });
    });
  }
});
