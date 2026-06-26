def test_get_book_by_id(client):

    book = client.post(
        "/books/",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "price": 14.99
        }
    ).json()

    response = client.get(f"/books/{book['id']}")

    assert response.status_code == 200
    assert response.json()["title"] == "The Great Gatsby"
    assert response.json()["author"] == "F. Scott Fitzgerald"
    assert response.json()["price"] == 14.99