#!/bin/bash
# send a JSON POST request and display the body of the response.
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
