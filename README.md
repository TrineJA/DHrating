Reading DH certificates and extracting ratings. Data is then visualized using Dash.

You can add a certificate by adding the certificate ID in `get_certificates.sh`

You can reset the base boat (your boat) in `src/app/data.py`

Otherwise, just run `make all`

## Heroku stuff
1) log in using heroku cli: `heroku login`
2) `heroku create APPNAME` to create your app (here APPNAME=dh-rating). This just needs to be done once.
3) `git push heroku master` will push your changes to heroku (it does NOT push to your git repo)

This will make your app run in 1 dyno (container).

Use `heroku open` to open your app (https://APPNAME.herokuapp.com/)

Use `heroku ps` to see how many dynos you have running (by your user).

Use `make heroku-local` to run locally (http://localhost:5000)