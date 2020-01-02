from flask import Flask

app = Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET')
def home():
    return "<h1>Distance Reading Archive</h1><p>This site is a prototype API for disatnce readingof science fiction novels.</p>"
