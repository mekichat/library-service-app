# tests/unit/test_get_books.py

   
def test_get_books(client):

    response = client.get("/books")

    assert response.status_code == 200
    assert isinstance(response.json(), list)