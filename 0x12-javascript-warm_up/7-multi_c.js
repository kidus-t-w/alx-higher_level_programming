#!/usr/bin/node
if (isNaN(parseInt(process.argv[2])) || process.argv[2] === null){
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('C is fun');
  }
}
