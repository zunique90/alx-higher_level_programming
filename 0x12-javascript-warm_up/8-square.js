#!/usr/bin/node
let i, c, r;
if (isNaN(process.argv[2]) === true) {
  console.log('Missing size');
}
for (i = 0; i < process.argv[2]; i++) {
  r = '';
  for (c = 0; c < process.argv[2]; c++) r += 'X';
  console.log(r);
}
