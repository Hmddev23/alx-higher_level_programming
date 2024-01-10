#!/usr/bin/node

const { dict } = require('./101-data');

const Arr = Object.entries(dict);
const newObject = {};
Arr.forEach(element => {
  newObject[element[1]] ? newObject[element[1]].push(element[0]) : newObject[element[1]] = [element[0]];
});

console.log(newObject);
