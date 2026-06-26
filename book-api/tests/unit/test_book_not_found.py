def test_book_not_found(client):

    response = client.get("/books/100")

    assert response.status_code == 404
    assert response.json()["detail"] == "Book not found"