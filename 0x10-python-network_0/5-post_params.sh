#!/bin/bash
# A script that takes a URL, sends a post request, and displays the body of response.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
