import pytest
from app.main import app as flask_app


# These are just simple tests, modify them as we go.
def test_home():
    response = flask_app.test_client().get('/')
    assert response.status_code == 200


def test_results():
    response = flask_app.test_client().get('/result')
    assert response.status_code == 200
