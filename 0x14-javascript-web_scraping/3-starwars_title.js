#!/usr/bin/node
// Your script description here

const reqURL = 'https://swapi-api.hbtn.io/api/films/'; // change 'let' to 'const'
const request = require('request'); // change 'let' to 'const'
request(reqURL + process.argv[2], function (error, response, body) {
  if (error) {
    console.error(error);
  } else {
    const jso = JSON.parse(body); // change 'let' to 'const'
    const results = jso.results; // change 'let' to 'const' and use dot notation
    let count = 0;
    for (let i = 0; i < results.length; i++) {
      const chars = results[i].characters; // change 'let' to 'const' and use dot notation
      for (let j = 0; j < chars.length; j++) {
        const check18 = chars[j].includes('18'); // change 'let' to 'const'
        if (check18) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
