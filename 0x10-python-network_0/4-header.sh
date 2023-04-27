#!/bin/bash
# A script that takes in URL as arg, sends a GET request and displays body of response
curl -sH "X-School-User-Id: 98" "$1"
