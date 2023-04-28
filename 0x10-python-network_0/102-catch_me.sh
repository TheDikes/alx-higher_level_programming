#!/bin/bash
# A script that makes a request to 0.0.0.0:5000/catch_me
curl -sL -X PUT -H "Content-Type: text/plain" -d "You got me!" http://0.0.0.0:5000/catch_me >/dev/null 2>&1 &
