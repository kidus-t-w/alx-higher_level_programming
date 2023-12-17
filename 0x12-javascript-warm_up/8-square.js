#!/usr/bin/node
num = process.argv[2];

if (isNaN(parseInt(num)) || num.length === 2) {
  console.log('Missing size');
} else {
  for (let i = 0; i < num; i++){
    myVal = '';
    for (let j = 0; j < num; j++){
      myVal = myVal + 'x';
    }
    console.log(myVal);
  }
}
