from flask import Flask, render_template
import gsheets
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('hello')
def hello():
    return 'Hello, World'


@app.route('user/<username>')
def show_user_profile(username):
# show the user profile for that user
    return 'User %s' % username


@app.route('post/<int:post_id>')
def show_post(post_id):
# show the post with the given id, the id is an integer
    return 'Post %d' % post_id


@app.route('path/<path:subpath>')
def show_subpath(subpath):
# show the subpath after /path/
    return 'Subpath %s' % subpath


@app.route('/projects/')
def projects():
    return 'The project page'


@app.route('/about')
def about():
    return 'The about page'

#
# books, posts = gsheets.main()
# books, posts = books[1:], posts[1:]
#
# book_dicts = []
# post_dicts = []
# for x in books:
#     book_dicts.append({
#     'book_id': x[0],
#     'book': x[1],
#     'author': x[2],
#     'book_cover': x[3],
#     })
#
# for y in posts:
#     post_dicts.append({
#     'book_id': y[0],
#     'post_author': y[1],
#     'post': y[2],
#     })
#
# @app.route('/')
# def index():
#     return render_template('index.html', books=book_dicts)
#

