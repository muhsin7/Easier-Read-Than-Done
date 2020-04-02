import gsheets
from flask import Flask, render_template
app = Flask(__name__)


books, posts = gsheets.main()
books, posts = books[1:], posts[1:]

book_dicts = []
post_dicts = []
for x in books:
    book_dicts.append({
    'book_id': x[0],
    'book': x[1],
    'author': x[2],
    'book_cover': x[3],
    })

for y in posts:
    post_dicts.append({
    'book_id': y[0],
    'post_author': y[1],
    'post': y[2],
    })

@app.route('/')
def index():
    return render_template('index.html', books=book_dicts)

@app.route('/book/<int:book_id>/')
def book(book_id):
    post_dict = [x for x in post_dicts if x['book_id']==str(book_id)]
    for i in book_dicts:
        if i['book_id'] == str(book_id):
            selected_book = i
    print(post_dict)
    return render_template('book.html', book_id=book_id, posts=post_dict, book=selected_book)

    # return render_template('book.html', book_id=book_id, post_dicts=post_dict)

if __name__ == '__main__':
   app.run(debug = True)
