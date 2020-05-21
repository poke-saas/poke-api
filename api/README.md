API Documentation
-
### Official API Documentation for Poke (for both your sake and mine)

The poke client consumes a REST API to manage and receive data for the frontend. This is a brief document
outlining which endpoints to use to accomplish specific tasks.

### API Structure:
#### Key: Curly braces denote a url {parameter}, otherwise all endpoints follow a tree structure. Click on a leaf node to view its documentation.
##### A check mark next to the endpoint means it has been implemented.
- /api
    - [x] [/test/](#testing-endpoint-test)
    - /firestore
        - /get
            - [x] [/{table}/{document name}/](#get-firestore-document-get)
        - [x] [/add/](#add-firestore-document-add)
        - [x] [/delete/](#delete-firestore-document-delete)
        - [x] [/update/](#update-firestore-document-update)
    - /auth
        - [x] [/login/](#user-login-login)
        - [ ] [/logout/](#user-logout-logout)
    - /services
        - [x] [/refresh/](#refresh-user-pokes-refresh)
        - [x] [/check/](#verify-that-a-poke-has-been-posted-check)
        
## Detailed Documentation

## Testing Endpoint (test)
- Purpose: To test if the api is up and running.
- Absolute URL: `/api/test/`
- Method Type: GET
- Body Format: N/A
- Response: Example JSON Response, sanity check.
- On fail: Error code 400

## Firestore Endpoints
For the *add* and *update* endpoints, I've made them smart. You don't have to explicitly declare what
kind of document you're updating or adding, it will automatically determine that information by
pattern matching the incoming JSON. ([List of valid JSON bodies here](#json-schemas).)

The *add* endpoint will also automatically update the organization's information with the reward, poke or user you're adding.

## Get Firestore Document (get)
- Purpose: To get firestore documents from the API as JSON.
- Absolute URL: `/api/firestore/get/{table}/{document id}`
- Method Type: GET
- Body Format: N/A
- Response: JSON Object containing object information in Firestore, based on URL Params.
- On fail: null body

## Add Firestore Document (add)
- Purpose: To add documents to firestore without direct console access.
- Absolute URL: `/api/firestore/add/`
- Method type: POST
- Body Format: JSON object containing required fields of an object you're trying to add ([list of valid JSON bodies here](#json-schemas).)
- Response: JSON Object containing object you've added to the firestore.
- On fail: null body

## Delete Firestore Document (delete)
- Purpose: To delete documents from firestore without direct console access.
- Absolute URL: `/api/firestore/delete/`
- Method Type: POST
- Body format: `{"table": "table_id", "document_id": "document_id"}`
- Response: JSON Object containing object removed from Firestore.
- On fail: null body

## Update Firestore Document (update)
- Purpose: To update firestore documents.
- Absolute url: `/api/firestore/update/`
- Method type: POST
- Body format: JSON object containing required fields of an object you're trying to update ([list of valid JSON bodies here](#json-schemas).)
- Response: JSON Object containing updated fields as they exist in firestore.
- On fail: null body

## User Login (login)
- Purpose: Load user information given correct credentials.
- Absolute URL: `/api/auth/login/`
- Method type: POST
- Body format: JSON Object containing username (email) and password of a valid user.
    - `{"uname": "username", "pwd": "password" }`
- Response: JSON Object of successfully logged in user.
- On fail: null body

## User Logout (logout)
- Purpose: To revoke user access token and clear local storage.
- Absolute URL: `/api/auth/logout/`
- Method type: POST
- Body format: JSON Object containing auth token.
    - `{"token": "eXaMpLetOkEn"}`
- Response: JSON Object containing success message.
- On fail: null body

## User Register (register)
- Deprecated, use add with a user object instead

## Refresh User Pokes (refresh)
- Purpose: To refresh the list of pokes available to the user.
- Absolute URL: `/api/services/refresh/`
- Method Type: POST
- Body Format: JSON Object containing User's ID (available from user object or access token).
    - `{"uid": "eXaMpLeuSeRID"}`
- Response: Updated list of pokes available to the user.
- On fail: null body

## Verify that a poke has been posted (check)
- Purpose: To verify that a user has posted a poke.
- Absolute URL: `/api/services/check/`
- Method Type: POST
- Body Format: JSON Object containing user's ID and the poke's ID.
    - `{"uid": "eXaMpleuSerID", "poke_id": "eXaMpLePOKeID"}`
- Response: JSON Object containing poke's status and number of points.
- On fail: null body


## JSON Schemas
Example User Schema:
```angular2
// After calling /api/auth/login/ and getting the "user" attribute
{
    "claimed_rewards_ids": [],
    "profile_picture_link": "na",
    "points": 0,
    "phone": "***-***-6950",
    "user_credentials": {
        "linkedin_uname": "na",
        "fb_uname": "na",
        "linkedin_pwd": "na",
        "ig_uname": "dakeenekid",
        "fb_pwd": "na",
        "twitter_pwd": "********",
        "ig_pwd": "********",
        "twitter_uname": "dakeenekid"
    },
    "org_id": "40a7a414ebe0bb5a40d190bbd43e4c40",
    "complete_pokes_ids": [
        "89c4eca957024766",
        "89c4eca957024766"
    ],
    "id": "5f0453ef3ae1caba5ed229f61965422a",
    "full_name": "dakeenekid"
}
```
Example Poke Schema:
```angular2
// After calling api/firestore/get/Pokes/[poke_id]
{
    "cta": "tw_tweet",
    "id": 12345,
    "deadline": "2020-03-01 12:00:00",
    "data": {
        "title": "HackIllinois Test Twitter",
        "body": "This is a test for Hack Illinois 2020!",
        "media": ""
    },
    "desc": "This is a test for HackIllinois 2020!",
    "name": "Twitter Test",
    "pts": 25
    "org_id": "[id of organization]"
}
```

Example Org Schema:
```angular2
// After calling api/firestore/get/Users/[user_id]
{
    "icon": "na",
    "reward_ids": [
        "6eb3ec5989704013",
        "zHhThm0r7B1UV1dB",
        "7741c99738a34ffb"
    ],
    "poke_ids": [
        "89c4eca957024766",
        "1f23cc23962142fb",
        "3401aee0bb324ec6",
        "9c100137db6943dc"
    ],
    "id": "40a7a414ebe0bb5a40d190bbd43e4c40",
    "user_ids": [
        "631209b539f14e32",
        "1076440981d44efb",
        "5f0453ef3ae1caba5ed229f61965422a",
        "94088de954c940d88a9d0fae1474595f"
    ],
    "name": "Founders"
}
```
Example Reward Schema:
```angular2
// After calling api/firestore/get/Rewards/[reward_id]
{
    "cost": 25,
    "id": "6eb3ec5989704013",
    "img": "https://www.bayshoreoutfitters.com/wp-content/uploads/2019/01/Better-Sweater-Jacket_Birch-White.jpg",
    "desc": "Brand new Patagonia jacket!",
    "name": "Patagonia Jacket"
    "org_id" "[id of organization]
}
```
