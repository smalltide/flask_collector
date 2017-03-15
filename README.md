# flask_collector
use python3, flask and PostgreSQL to create a data collect web app and deploy to heroku

1. python3
2. flask
3. PostgreSQL

```
  > git@github.com:smalltide/flask_collector.git
  > cd flask_collector
  > pip3 install flask
  > pip3 install psycopg2
  > pip3 install Flask-SQLAlchemy
  > createdb -O ice height_collector
  > from app import db
  > db.create_all()
  > python3 app.py
```

if need virtualenv and deploy to Heroku
```
  > cd flask_collector
  > pip3 install virtualenv
  > python3 -m venv venv
  > venv/bin/pip3 install flask
  > venv/bin/pip3 install psycopg2
  > venv/bin/pip3 install Flask-SQLAlchemy
  > createdb -O ice height_collector
  > from app import db
  > db.create_all()
  > venv/bin/python3 app.py
```

if deploy to Heroku
```
  > venv/bin/pip3 install gunicorn
  > venv/bin/pip3 freeze > requirements.txt
  > echo "web: gunicorn app:app" > Procfile
  > echo "python-3.6.0" > runtime.txt
  > heroku login
  > heroku create flask-collector
  > heroku addons:create heroku-postgresql:hobby-dev --app flask-collector
  > heroku config --app flask-collector
  > heroku git:remote -a flask-collector
  > git push heroku master
  > heroku run bash or heroku run python
  > from app import db
  > db.create_all()
  > heroku pg:psql --app flask-collector
  > heroku open
```
