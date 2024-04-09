#!/usr/bin/node

// Converts a number from base 10 to a base passed by argument

exports.converter = function (base) {
  function myCovert (n) {
    return n.toString(base);
  }

  return myCovert;
};
