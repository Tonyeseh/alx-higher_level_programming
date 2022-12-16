#!/bin/bash
# sends a JSON POST request to a URL passed and JSON file passed as seconds arg
curl -s -H "Content-Type: application/json" -d @$2 $1
