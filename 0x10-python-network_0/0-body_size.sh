#!/usr/bin/bash
# Bash script that takes in a URL, 
# sends a request to that URL,
# and displays the size of the body of the response 

url="$1"
response_body=$(curl -s "$url")
size=$(echo -n "$response_body" | wc -c)
echo "The size of the response body is $size bytes."
