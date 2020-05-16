# Poke REST API
Internal API used by Poke to augment and receive data to the application.

## Getting Started Locally
To run poke's API locally, you need to acquire a _service account credentials file_
to gain access to the Google Firestore. The only endpoint that will work without this credentials file
is the testing one. To obtain this file, <b>contact a developer of the project</b>.

Before continuing, make sure you're using Python 3 and a UNIX based machine. Otherwise, feel free to run this [non-locally](#getting-started-on-the-cloud) instead.

Once the file is obtained, place it under `scripts/` and change the `path` variable in `scripts/authenticate.sh`
to match the _absolute_ path of the config.

You'll also need to download the [Google Cloud SDK](https://cloud.google.com/sdk) for your operating system for the below
script to work.

Run the auth script (source it with `. scripts/authenticate.sh`), and you should have the `GOOGLE_APPLICATION_CREDENTIALS` variable set.
Verify that this points to your config file before continuing.

Verify that the service account is authorized on your machine by running `gcloud info` and seeing the `account` property set as a google service account.

Once that's all set up, install dependencies by running `pip install -r requirements.txt`.

Finally, start the server by running `python manage.py runserver` inside of the `api/` project root.

## Getting Started on the Cloud
This API is dockerized for convenience, and running on a DigitalOcean Droplet.
To use the API non-locally, send requests to the following URL:
`[where I'll put hosted url]`.

## Usage
For a detailed API Documentation, view the [API Project README](https://github.com/poke-saas/poke-api/blob/master/api/README.md).