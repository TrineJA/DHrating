Reading DH certificates and extracting ratings. Data is then visualized using Dash.

You can add a certificate by adding the certificate ID in `get_certificates.sh`

You can reset the base boat (your boat) in `src/app/data.py`

Otherwise, just run `make all`

## Heroku stuff
1) login in using heroku cli: `heroku login`
2) `heroku create APPNAME` to create your app (here APPNAME=dh-rating)
3) `git push heroku master` (this will ONLY push to heroku and NOT your git repo)

This will make your app run in 1 dyno (container).
`heroku open` will open your app (from https://APPNAME.herokuapp.com/)
Use `heroku ps` to see how many dynos you have running.
Use `make heroku-local` to run locally ( http://localhost:5000)