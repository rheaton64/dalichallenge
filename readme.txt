Code for 22W Dali Lab API Challenge

This is an API that has basic GET and POST functionality for both the public and anonymous data sets provided

API endpoints are as follows:
(url)/api...

- GET /data/(pub/anon/all)/all: returns entire JSON of the specified data set (either pub, anon, or both)

- GET /data/(pub/anon/all)?...: returns data from the specified data set that matches the given query parameters(ex. /data/pub?year='22)

-POST /data/(pub/data)...: posts the body data of the request into the specified data set