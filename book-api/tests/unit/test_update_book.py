def test_update_book(client):

    create_response = client.post(
        "/books/",
        json={
            "title": "Dune",
            "author": "Frank Herbert",
            "price": 25.5
        }
    )

    book_id = create_response.json()["id"]

    response = client.put(
        f"/books/{book_id}",
        json={
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "price": 14.99
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert data["title"] == "The Great Gatsby"
    assert data["author"] == "F. Scott Fitzgerald"
    assert data["price"] == 14.99