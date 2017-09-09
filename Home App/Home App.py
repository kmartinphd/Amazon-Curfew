from flask import Flask, render_template
from flask_ask import Ask, question, statement


app = Flask(__name__)
ask = Ask(app, "/")

@app.route("/")
def homepage():
    """
    gives a homepage for the app. app is hosted over port 5000 since this is a Flask app. This can be used for testing to
    ensure the server is online
    :return: message text to be posted
    """
    return render_template("index.html")