''' Main.py for executing my website'''
from flask import Flask, render_template




app = Flask(__name__)

@app.route('/')  #home page
def index():
    return render_template('index.html')

@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')


if __name__ == '__main__':
    app.run(debug=True)
