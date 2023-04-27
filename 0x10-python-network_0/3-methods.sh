#!/bin/bash
# A bash script that displays all HTTP methods
curl -sI "$1" | grep -i allow | cut -d' ' -f2-
