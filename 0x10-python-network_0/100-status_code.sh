#!/bin/bash
# displays the status code of the response only
curl -s -o /dev/null -w '%{response_code}' $1
