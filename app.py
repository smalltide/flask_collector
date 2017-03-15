from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func

app = Flask(__name__)
#app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://ice:123456@127.0.0.1/height_collector"
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://bhevmhlgehwvzx:ef6feb25a811bb62030111edbb3d44c9f6babffb0bc4025b37cde3f1ed5bb3f5@ec2-54-243-187-133.compute-1.amazonaws.com:5432/d3uch9tf609bej?sslmode=require"
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(120), unique = True)
    height = db.Column(db.Integer)

    def __init__(self, email, height):
        self.email = email
        self.height = height


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method == "POST":
        email = request.form["email_name"]
        height = request.form["height_name"]

        if db.session.query(Data).filter(Data.email == email).count() == 0:
            data = Data(email, height)
            db.session.add(data)
            db.session.commit()
            average_height = db.session.query(func.avg(Data.height)).scalar()
            average_height = round(average_height, 1)
            count = db.session.query(Data.height).count()
            send_email(email, height, average_height, count)
            return render_template("success.html")
    return render_template("index.html", text = "Seems like we've got something from that email address already!")


if __name__ == "__main__":
    app.debug = True
    app.run()
