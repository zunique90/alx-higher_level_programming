#!/usr/bin/node
if (isNaN(process.argv[2]) === true) {
  console.log('Not a number');
} else {
  const num = parseInt(process.argv[2], 10);
  console.log('My number: ' + num);
}
