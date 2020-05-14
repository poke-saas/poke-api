#!/bin/bash

export GOOGLE_APPLICATION_CREDENTIALS=config.json
gcloud auth activate-service-account --key-file=config.json