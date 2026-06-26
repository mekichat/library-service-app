def test_delete_book(client):

    create_response = client.post(
        "/books/",
        json={
            "title": "Dune",
            "author": "Frank Herbert",
            "price": 25.5
        }
    )

    book_id = create_response.json()["id"]

    response = client.delete(f"/books/{book_id}")

    assert response.status_code == 200

    get_response = client.get(f"/books/{book_id}")

    assert get_response.status_code == 404