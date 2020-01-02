from flask import Flask
from flask import request,jsonify

app = Flask(__name__)
app.config["DEBUG"] = True

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



app.run()
