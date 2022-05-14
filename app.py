from flask import Flask, render_template
from data import text_example


app = Flask(__name__)

@app.route("/")
def home():
    return render_template('homepage.html')

@app.route("/history")
def history():
    return render_template('history.html', texts = text_example, title = 'My Searches')

