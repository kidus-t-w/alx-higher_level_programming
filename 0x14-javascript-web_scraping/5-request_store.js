#!/usr/bin/node
// A script that gets the contents of a webpage

const fs = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));
