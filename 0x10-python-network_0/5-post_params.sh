#!/bin/bash
# A script that takes a URL, sends a post request to the passed URL, and displays the body of response.
curl -X POST -d 'email="test@gmail.com"&subject="I will always be here for PLD"' "$1"
