#!/usr/bin/node
const dict1 = require('./101-data').dict;
let res = {};
for (let key in dict1) {
  if (res[dict1[key]] === undefined) {
    res[dict1[key]] = [key];
  } else {
  res[dict1[key]].push(key);

  }
}
console.log(res);
