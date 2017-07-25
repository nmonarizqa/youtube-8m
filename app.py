from flask import Flask, redirect, render_template, request, url_for, abort
from datetime import datetime
app = Flask(__name__)

@app.route('/')
def homepage():
    # the_time = datetime.now().strftime("%A, %d %b %Y %l:%M %p")
    #
    # return """
    # <h1>Your Beauty Guru Recommendation</h1>
    # <p>This app is in progress. Here are the initial explorations</p>
    # """
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
