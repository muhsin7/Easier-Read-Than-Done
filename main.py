from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/book/<book>')
def book(title):
    return render_template('flush.html')

if __name__ == '__main__':
   app.run(debug = True)
