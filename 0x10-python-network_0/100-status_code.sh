#!/bin/bash
# send a request and display only the status code
curl -s -o /dev/null -I --w "%{http_code}" "$1"
