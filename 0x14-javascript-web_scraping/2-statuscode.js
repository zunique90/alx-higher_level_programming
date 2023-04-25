#!/usr/bin/node
// This script displays the status code of a `GET` request

const request = require('request');
request.get(process.argv[2], function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + data.statusCode);
  }
});
