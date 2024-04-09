#!/usr/bin/node

// Returns the number of occurrences of an element in a list

exports.nbOcurrences = function (list, searchElement) {
  return list.filter(x => x === searchElement).length;
};
