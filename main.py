#This file is responsible for running the web server and (mostly nothing else)
from flask import Flask, render_template, session, redirect, url_for
from defaults import *
from functions import *
from config import *

app = Flask(__name__)
session = ServSession

@app.route("/")
def home():
    return redirect(url_for("dash"))

@app.route("/dash/")
def dash():
    return render_template("dash.html", title="Dashboard", session=session)



app.run(port=UserConfig["Port"])