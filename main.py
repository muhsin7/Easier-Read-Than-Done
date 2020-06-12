from flask import Flask, render_template, request, redirect, url_for, abort
import pyrebase
import os
config = {
    'apiKey': "<key>",
    'authDomain': "<domain>",
    'databaseURL': "<url>",
    'projectId': "easier-read-than-done",
    'storageBucket': "<bucket>",
    'messagingSenderId': "<id>",
    'appId': "<addId>",
    'measurementId': "<measurementId>"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
storage = firebase.storage()
app = Flask(__name__)

def get_posts(id):
    all_posts = db.child('posts').get().each()
    book_posts = []
    for x in all_posts:
        if int(x.val()['book_id']) == id:
            book_posts.append(x)

    return book_posts


all_books = db.child('books').get().each()
def get_book(id):
    for x in all_books:
        if x.val()['book_id'] == id:
            selected_book = x
    return selected_book

def increment_id():
    last_book = all_books[-1]
    return int(last_book.val()['book_id'])+1

@app.route('/')
def index():
    books = db.child('books').get()
    return render_template('index.html', books=books.each())\

# @app.errorhandler(404)
# def pagenotfound(e):
#     return render_template('404.html'), 404

@app.route('/book/<int:book_id>/', methods=['GET', 'POST'])
def book(book_id):
    try:
        book = get_book(book_id)
        posts = get_posts(book_id)
        return render_template('book.html', book_id=book_id, posts=posts, book=book)
    except UnboundLocalError:
        abort(404)
        # return render_template(url_for('index'))
    # return render_template('book.html', book_id=book_id)
    # return render_template('book.html', book_id=book_id, post_dicts=post_dict)

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        post = request.form['post_content']
        author = request.form['post_author']
        book_id = int(request.form['book_id'])
        db.child('posts').push({'book_id':book_id, 'post_author': author, 'post': post})
        return redirect(url_for('book', book_id=book_id))
    # book_id = request.form['book_id']
    # return render_template('book.html', book_id=book_id, posts=get_posts(book_id), book=get_book(book_id))

@app.route('/newbook', methods=['GET', 'POST'])
def newbook():
    if request.method == 'POST':
        book = request.form['book_name']
        author = request.form['author_name']
        book_id = increment_id()
        file = request.form['cover']
        newFile = FileContents(name=file.filename, data=file.read())
        # file = request.form.get("book_cover")
        name = (f'/{book}_{author.split()[0]}_{str(book_id)}.jpeg').lower()
        storage.child(name).put(file)
        print(file, type(file))
        db.child('books').push({'book_id':book_id, 'author': author, 'book': book, 'cover': name})
        return redirect(url_for('index'))

if __name__ == '__main__':
   # app.run(debug = True)
   app.run(debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)))
