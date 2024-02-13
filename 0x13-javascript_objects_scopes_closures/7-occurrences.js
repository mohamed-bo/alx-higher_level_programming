#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  for (const e of list) {
    if (e === searchElement) {
      count++;
    }
  }
  return count;
};
