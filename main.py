from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('Home.html')


@app.route('/author')
def author():
    return render_template('Author.html')

@app.route('/latest')
def latest():
    return render_template('Latest.html')

@app.route('/search')
def search():
    return render_template('Search.html')

if __name__ == '__main__':
    app.run(debug=True)
