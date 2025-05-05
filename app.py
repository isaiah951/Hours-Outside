import os
import sqlite3
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Define a route for the homepage
@app.route('/')
def home():
    return "<h1>Welcome to Hours-Outside!</h1>"

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
