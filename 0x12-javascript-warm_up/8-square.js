#!/usr/bin/node
const square_size = Math.floor(Number(process.argv[2]));
if (isNaN(square_size)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < square_size; r++) {
    let row = '';
    for (let c = 0; c < square_size; c++) row += 'X';
    console.log(row);
  }
}
