# How to Deploy App with Heroku
2018-10-12

1. Make sure you have pipenv installed with requirements.txt and Pipfile, Pipfile.lock files.

2. Create a 'Procfile'. (example content that would go with Flask is 'web: gunicorn application:app', add gunicorn to requirements.txt)

3. (At the directory you want to deploy), run 'heroku login' or just go straight to 'heroku create'.

4. Run 'git remote -v' to check if remote heroku repository is created.

5. Run 'git push heroku master' to push your local files to heroku.

6. Run 'heroku open' to open your app in browser.

### Heroku commands
- heroku git:remote -a app
(You can use heroku CLI in that directory without specifying the app name)
- heroku config
- heroku config:set DATABASE_URL=<URL>
- heroku config:unset DATABASE_URL
- heroku logs --tail
- heroku ps [-a app]
- heroku ps:restart/stop (if 'web' is not specified, restarts/stop all dynos on app)
- heroku apps:rename newname (rename your app to newname)
- git remote remove heroku (delete heroku remote from your directory)
- heroku git:remote -a newname (add heroku remote of newname)
- herou git:clone [directory]
- heroku local (optional)[PROCESSNAME/dyno]
- heroku maintenance:on/off
- heroku pg (optional)[DATABASE] (database info)
- heroku config:set DATABASE_URL=$(heroku config:get DATABASE_URL -a your-app) your_process