#!/bin/bash
# Script that sends a JSON POST request to a URL and displays the body of the response
curl -sX POST -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
