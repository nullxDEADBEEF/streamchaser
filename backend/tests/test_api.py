from fastapi.testclient import TestClient
from backend.src import main

client = TestClient(main.app)


def test_get_correct_movie_from_id():
    response = client.get('/dk/movie/120')
    assert response.status_code == 200
    assert response.json().get('title') == 'The Lord of the Rings: The Fellowship of the Ring'


def test_get_correct_tv_from_id():
    response = client.get('/dk/tv/120')
    assert response.status_code == 200
    assert response.json().get('name') == 'Andy Capp'
