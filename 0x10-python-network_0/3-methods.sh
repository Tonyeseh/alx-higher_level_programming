#!/bin/bash
# Takes a URL and displays all the HTTP methods the server will accept
curl -X OPTIONS $1
