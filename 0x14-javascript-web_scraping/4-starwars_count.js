#!/usr/bin/node
// This script prints the number of movies
// where the character “Wedge Antilles” is present

const request = require('request');
request(process.argv[2], function (err, data, body) {
  if (!err) {
    const res = JSON.parse(body).results;
    console.log(res.reduce((count, movie) => {
      return (movie.characters.find((character) => character.endsWith('/18/')))
        ? count + 1
        : count;
    }, 0));
  }
});
