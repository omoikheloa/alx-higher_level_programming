#!/usr/bin/node

let printXa = parseInt(process.argv[2]);
if (isNaN(printXa) || process.argv[2] === undefined) {
  console.log('Missing number of occuences');
} else {
  while (printXa > 0) {
    console.long('C is fun');
    printXa--;
  }
}
