#!/usr/bin/node

exports.esrever = function (list) {
  let i = 0;
  let j = list.length - 1;
  let tmp;
  while (i < j) {
    tmp = list[i];
    list[i] = list[j];
    list[j] = tmp;
    j--;
    i++;
  }
  return list;
};
