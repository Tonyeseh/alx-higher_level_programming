#!/bin/bash
# displays the size of the body of a respnse to a curl request
curl -s $1 | wc -c
