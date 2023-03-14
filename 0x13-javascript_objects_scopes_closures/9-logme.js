#!/usr/bin/node
let numargs = 0;
exports.logMe = function (item) {
  console.log(`${numargs}: ${item}`);
  numargs += 1;
};
