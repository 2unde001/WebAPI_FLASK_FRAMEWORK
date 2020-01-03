from flask import Flask
from flask import request,jsonify
import sqlite3

app = Flask(__name__)
app.config["DEBUG"] = True

def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d

"""
Create a dictionaries test data for our catalog
"""

books = [
  { 'id':0,
    'title':'A Fire Uponthe Deep',
    'author':'Vennor Vinge',
    'first_sentence':'he coldsleep itself was a dreamless.',
    'year_published':'1992'
    },

    { 'id':1,
      'title':'The Ones Who Walk Away From Omelas',
      'author':'Ursula K. Le Guin',
      'first_sentence':'With a clamor of bell that set the swallows soaring,the Festival of Summer came to the city Omelas bright-towered by the sea.',
      'published':'1973'
      },

      { 'id':2,
      'title':'Dhalgren',
      'author':'Samuel R Delany',
      'first_sentence':'to wound the autumnal city',
      'published':'1975'

      }
]

@app.route('/', methods=['GET'])
def home():
    return "<h1>Distance Reading Archive</h1><p>This site is a prototype API for disatnce readingof science fiction novels.</p>"

@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
     return jsonify(books)

@app.route(404):
def page_not_found(e):
    return '<h1>404<h1/><p>The resources could not be found,</p>',404


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    """
    Check if an ID was provided as part of the Url
    Assign ID provided to a variable and if ID not provided throw an error
    If ID is not provided, display an error in the browser

    """

    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return 'Error: No id field provided. Please specify an id.'

    # Create an empty list for result
    results = []

    for book in books:
        if book['id'] == id:
            results.append(book)

    # add result to jsonify funcion
    return jsonify(results)

app.run()
