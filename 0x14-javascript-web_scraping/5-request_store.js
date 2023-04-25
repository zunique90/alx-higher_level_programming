#!/usr/bin/node
// This script gets the contents of a webpage and stores it in a file

const request = require('request');
const fs = require('fs');
request(process.argv[2], function (err, data, body) {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err, dat) {
      if (err) {
        console.log(err);
      }
    });
  }
});
