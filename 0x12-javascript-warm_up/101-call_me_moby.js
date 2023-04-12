#!/usr/bin/node
//This function is visible from outside and executes x times a function

function callMeMoby(x, theFunction) {
  for(let i = 0; i < x; i++) {
    callMeMoby();
  }
   
  exports = callMeMoby
