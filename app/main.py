from flask import (Flask,
                   render_template)


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/result')
def results():
    return render_template('results.html', fnews_web_result_content="<h2>This is for testing purpose, "
                                                                    "you can pass results here</h2>")
                                                                    