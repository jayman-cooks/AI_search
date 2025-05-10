from flask import Flask, render_template, request
from make_query import make_query

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        links = make_query(query)
        return render_template('results.html', query=query, links=links)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
