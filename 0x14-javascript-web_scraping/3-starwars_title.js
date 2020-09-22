#!/usr/bin/node
const request = require('request');
const _Id = process.argv[2];
const baseUrl = `https://swapi-api.hbtn.io/api/films/${_Id}`;
request(baseUrl, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
