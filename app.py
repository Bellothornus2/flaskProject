from flask import Flask, jsonify, request
import rand_string.rand_string as rand

app = Flask(__name__)

books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/')
def hello_world():
    return 'Hello World!' + rand.RandString("uppercase", 10)


@app.route("/api/v1/resources/books/all", methods=["GET"])
def allBooks():
    return jsonify(books)

@app.route("/api/v1/resources/books/insertone", methods=["GET","POST"])
def saveBooks():
    id = 3
    title = 'Nuevo Libro'
    author = 'Aquel Borracho'
    sentence = 'Escribí el libro porque me apetecía.'
    publish = '2020'
    new_book = {
        'id': id,
        'title': title,
        'author': author,
        'first_sentence': sentence,
        'published': publish
    }
    books.append(new_book)

@app.route("/api/v1/resources/books/insertcustom", methods=["GET","POST"])
def saveCustomBook():
    id = 4
    title = request.args.get("title")
    author = request.args.get("author")
    sentence = request.args.get("sentence")
    publish = request.args.get("publish")
    new_book = {
        'id': id,
        'title': title,
        'author': author,
        'first_sentence': sentence,
        'published': publish
    }
    books.append(new_book)
    return jsonify(books)

@app.route("/login")
def login():
    username = request.args.get("username")
    password = request.args.get("pasword")


if __name__ == '__main__':
    app.run()
