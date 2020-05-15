#!/bin/bash

# Replace this path variable with where you keep your Google Cloud Application credentials file
path=/Users/davis/github/poke-api/scripts/config.json
export GOOGLE_APPLICATION_CREDENTIALS=$path
echo $GOOGLE_APPLICATION_CREDENTIALS
gcloud auth activate-service-account --key-file=$path