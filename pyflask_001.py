from flask import Flask

app = Flask(__name__)

@app.route('/')
def  index():
    return "</h1> Flask 001 - Hi </h1>"