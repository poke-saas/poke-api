API Documentation
-
### Official API Documentation for Poke (for both you sake and mine)

The poke client consumes a REST API to manage and receive data for the frontend. This is a brief document
outlining which endpoints to use to accomplish specific tasks.

### API Structure:
#### Key: Curly braces denote a url {parameter}, otherwise all endpoints follow a tree structure. Click on a leaf node to view its documentation.
- /api
    - [/test/](#testing-endpoint-test)
    - /firestore
        - /get
            - [/{table}/{document name}/](#get-firestore-document-get)
        - [/add/{table}/](#add-firestore-document-add)
        - [/delete/{table}/](#delete-firestore-document-delete)
        - [/update/{table}/{document name}](#update-firestore-document-update)
    - /auth
        - [/login/](#user-login-login)
        - [/logout/](#user-logout-logout)
    - /services
        - [/refresh/](#refresh-user-pokes-refresh)
        - [/check/](#verify-that-a-poke-has-been-posted-check)
        
        
## Detailed Documentation

## Testing Endpoint (test)
- Purpose: To test if the api is up and running.
- Absolute URL: /api/test/
- Method Type: GET
- Body Format: N/A
- Response: Example JSON Response, sanity check.
- On fail: Error code 400

## Get Firestore Document (get)
- Purpose: To get firestore documents from the API as JSON.
- Absolute URL: /api/firestore/get/{table}/{document id}
- Method Type: GET
- Body Format: N/A
- Response: JSON Object containing object information in Firestore, based on URL Params.
- On fail: null body

## Add Firestore Document (add)
- Purpose: To add documents to firestore without direct console access.
- Absolute URL: /api/firestore/add/{table}
- Method type: POST
- Body Format: JSON object containing required fields of an object you're trying to add ([list of valid JSON bodies here](#valid-json-body-outlines).)
- Response: JSON Object containing object you've added to the firestore.
- On fail: null body

## Delete Firestore Document (delete)
- Purpose: To delete documents from firestore without direct console access.
- Absolute URL: /api/firestore/delete/{table}/{document id}
- Method Type: POST
- Body format: None required.
- Response: JSON Object containing object removed from Firestore.
- On fail: null body

## Update Firestore Document (update)
- Purpose: To update firestore documents.
- Absolute url: /api/firestore/update/{table}/{document id}
- Method type: POST
- Body format: JSON Object containing updated fields of an object in firestore.
- Response: JSON Object containing updated fields as they exist in firestore.
- On fail: null body

## User Login (login)
- Purpose: Load user information given correct credentials.
- Absolute URL: /api/auth/login/
- Method type: POST
- Body format: JSON Object containing username (email) and password of a valid user.
    - {"uname": "username", "pwd": "password" }
- Response: JSON Object of successfully logged in user.
- On fail: null body

## User Logout (logout)
- Purpose: To revoke user access token and clear local storage.
- Absolute URL: /api/auth/logout/
- Method type: POST
- Body format: JSON Object containing auth token.
    - {"token": "eXaMpLetOkEn"}
- Response: JSON Object containing success message.
- On fail: null body

## Refresh User Pokes (refresh)
- Purpose: To refresh the list of pokes available to the user.
- Absolute URL: /api/services/refresh/
- Method Type: POST
- Body Format: JSON Object containing User's ID (available from user object or access token).
    - {"uid": "eXaMpLeuSeRID"}
- Response: Updated list of pokes available to the user.
- On fail: null body

## Verify that a poke has been posted (check)
- Purpose: To verify that a user has posted a poke.
- Absolute URL: /api/services/check/
- Method Type: POST
- Body Format: JSON Object containing user's ID and the poke's ID.
    - {"uid": "eXaMpleuSerID", "poke_id": "eXaMpLePOKeID"}
- Response: JSON Object containing poke's status and number of points.
- On fail: null body


## Valid JSON Body Outlines
Going to write these later, if you need them they can be found as dataclasses under _poke_main/models.py_