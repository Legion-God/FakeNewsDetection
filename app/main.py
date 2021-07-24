from flask import (Flask,
                   render_template, request)
from pathlib import Path
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

app = Flask(__name__)

# Load the model and vectorizer vocabulary

model_path = Path(__file__).parent.parent/"Model"
trained_model = pickle.load(open(model_path/"model.pkl", "rb"))
trained_tfidf = pickle.load(open(model_path/"tfidf.pkl", "rb"))


@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def predict():
    x = request.form['inputUrl']
    x = [x]
    vectorized_x = trained_tfidf.transform(x)
    y = trained_model.predict(vectorized_x)[0]

    return render_template('index.html', prediction=y)


@app.route('/result')
def results():
    return render_template('results.html', fnews_web_result_content="<h2>This is for testing purpose, "
                                                                    "you can pass results here</h2>")
