#!/bin/bash
# send a GET request with header variable 'X-School-User-Id' with variable 98
curl -sH "X-School-User-Id: 98" "$1"
