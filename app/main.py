from flask import (Flask,
                   render_template, request)

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    input_claim = request.form['inputUrl']
    return render_template('index.html', prediction=input_claim)


@app.route('/result')
def results():
    return render_template('results.html', fnews_web_result_content="<h2>This is for testing purpose, "
                                                                    "you can pass results here</h2>")
