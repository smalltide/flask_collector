# flask_collector
use python3, flask and PostgreSQL to create a data collect web app and deploy to heroku

![alt text](https://github.com/smalltide/flask_collector/blob/master/screenshot.gif "flask_collector")

1. python3
2. flask
3. PostgreSQL

```
  > git@github.com:smalltide/flask_collector.git
  > cd flask_collector
  > pip3 install flask
  > python3 app.py
```

if need virtualenv and deploy to Heroku
```
  > cd flask_collector
  > pip3 install virtualenv
  > python3 -m venv venv
  > venv/bin/pip3 install flask
  > venv/bin/python3 web.py
```

if deploy to Heroku
```
  > venv/bin/pip3 install gunicorn
  > venv/bin/pip3 freeze > requirements.txt
  > echo "web: gunicorn web:app" > Procfile
  > echo "python-3.6.0" > runtime.txt
  > heroku login
  > heroku create flask-collector
  > heroku git:remote -a flask-collector
  > git push heroku master
```
