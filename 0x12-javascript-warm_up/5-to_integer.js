#!/usr/bin/node
const nbr = Math.floor(Number(process.argv[2]));
console.log(isNaN(nbr) ? 'Not a number' : `My number: ${nbr}`);
