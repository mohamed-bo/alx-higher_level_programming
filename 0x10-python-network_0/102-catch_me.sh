#!/bin/bash
#Send a request
curl -s -L -X PUT -d "user_id=98" -H "Origin: Alx" 0.0.0.0:5000/catch_me
