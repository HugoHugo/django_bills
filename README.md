# Django Bills - my mini example API in Django

## First time use

Run the command below

```
python manage.py migrate
python manage.py runserver

curl --location --request GET 'http://127.0.0.1:8000/'
```

Expect this response for the basic index call:
```
{"metadata": {}, "content": "Welcome to bills app"}
```

## DB

Since this is an example project it uses SQL Lite as its database. Be careful, this is not a suitable DBMS for production. 

## Static Files

Since this is an example project it uses the default Django static file server. This server is rather insecure and can place an unreasonable load on the web app if your use case involves large file transfers (like background graphics/images/etc.).

## Media Files

These are currently also handled through the static file handler, which is again not suited for this use case. Use a cloud bucket that allows the client's browser/API to upload directly to the bucket instead of using Django for file uploads.

## Env Vars

To protect your web app in production, please generate (and safe keep forever) a Django secret key `SECRET_KEY`. Set `RUNTIME_ENV` to one of local/dev/stg/prod keeping in mind 'local' means Django's DEBUG is allowed. Set `LOG_LEVEL` to any of the standard values. Furthermore, set your `ALLOWED_HOSTS` URL to the proper host for each `RUNTIME_ENV`, this is an important step in securing your web app.

```
export SECRET_KEY="generate-me"
export RUNTIME_ENV=""
export LOG_LEVEL=""
export ALLOWED_HOSTS="['one.com','ormore.com']"
```