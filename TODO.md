TODO
-

This is a document to just go over things that need to get done for the API to work.
Most of the code has been written already in the form of google cloud functions, so the task here is to refactor these large functions into a scalable
API instead, making it easier and more intuitive to get data and work with data in the firestore.

### TODO (deadline: Friday, May 15th)
- [x] Move over db utils and get authentication working through poke's service account
- [x] Seperate project into several apps based on functionality.
- [x] Create dataclasses for the serialization of objects stored in firestore.

### TODO (deadline: Friday, May 22nd)
- [ ] Finish API endpoints for managerial console (add, delete, update)
- [ ] Implement JWT Token Authentication for signed in users
- [ ] Enforce HTTPS (Let's Encrypt SSL)
- [ ] Write unit tests to verify endpoints are working and to test edge cases


