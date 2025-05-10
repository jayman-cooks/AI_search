from flask import Flask, render_template, request
from make_query import make_query

app = Flask(__name__)

# Mock function to simulate link fetching
def get_links_for_query(query):
    # You'd replace this with your real function
    return [
        f"https://example.com/search?q={query}&result=1",
        f"https://example.com/search?q={query}&result=2",
        f"https://example.com/search?q={query}&result=3"
    ]

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        query = request.form['query']
        links = make_query(query)
        return render_template('results.html', query=query, links=links)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
