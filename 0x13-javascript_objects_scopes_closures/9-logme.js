#!/usr/bin/node
let arg_counter = 0;
exports.logMe = function (item) { console.log(`${arg_counter++}: ${item}`); };
