#!/usr/bin/node
let i;
if (isNaN(process.argv[2]) === true) {
  console.log('Missing number of occurrences');
}
for (i = 0; i < process.argv[2]; i++) {
  console.log('C is fun');
}
