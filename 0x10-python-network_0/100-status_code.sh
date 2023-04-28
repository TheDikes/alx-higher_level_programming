#!/bin/bash
# A script that sends a request URL and displays only status code
curl -so /dev/null -w "%{http_code}" "$1"
