def test_create_book(client):

    payload = {
        "title": "Dune",
        "author": "Frank Herbert",
        "price": 25.5
    }

    response = client.post("/books/", json=payload)

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == payload["title"]
    assert data["author"] == payload["author"]
    assert data["price"] == payload["price"]