#!/bin/bash
# Sets params for a POST request.
curl -sd "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
