from flask import (Flask,
                   render_template, request)
from pathlib import Path
import pickle
import validators
from newspaper import Article

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
    if validators.url(x):
        # input is url then download, parse the extract the text from article.

        try:
            article = Article(x)
            article.download()
            article.parse()
            x = article.text
        except:
            error_message = f"Oops!, something went wrong. Maybe article is dead or Check your internet connection."
            return render_template('index.html', error_message=error_message)

    x = [x]
    vectorized_x = trained_tfidf.transform(x)
    y = trained_model.predict(vectorized_x)[0]
    return render_template('index.html', prediction=y)


@app.route('/result')
def results():
    return render_template('results.html', fnews_web_result_content="<h2>This is for testing purpose, "
                                                                    "you can pass results here</h2>")
