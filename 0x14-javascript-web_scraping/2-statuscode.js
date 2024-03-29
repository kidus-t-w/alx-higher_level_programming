#!/usr/bin/node
// Display the status code of a GET request

const args = process.argv;
const request = require('request'); // change 'let' to 'const'
request(args[2], function (error, response, body) {
  if (error) {
    console.log('error:', error); // Print the error if one occurred
  } else console.log('code:', response && response.statusCode);
});
