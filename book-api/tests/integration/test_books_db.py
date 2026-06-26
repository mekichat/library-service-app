# tests/integration/test_books_db.py

def test_database_persistence(client):

    payload = {
         "title": "Pride and Prejudice",
         "author": "Jane Austen",
         "price": 9.99
    }
    
    response = client.post("/books/", json=payload)

    assert response.status_code == 200

    book_id = response.json()["id"]

    response = client.get(f"/books/{book_id}")

    assert response.status_code == 200
    assert response.json()["title"] == "Pride and Prejudice"
    assert response.json()["author"] == "Jane Austen"
    assert response.json()["price"] == 9.99
    
    
