#!/bin/bash
# send a POST request to the URL with specified parameters
# and display the body of the response.
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
