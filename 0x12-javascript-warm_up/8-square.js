#!/usr/bin/node
const square = Math.floor(Number(process.argv[2]));
if (isNaN(square)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < square; r++) {
    let row = '';
    for (let c = 0; c < square; c++) row += 'X';
    console.log(row);
  }
}
