#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight(function (list, curr) {
    list.push(curr);
    return list;
  }, []);
};
