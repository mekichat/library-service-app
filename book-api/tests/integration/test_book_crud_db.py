def test_full_book_crud_flow(client):

    # CREATE    
    payload_create = {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "price": 9.99
    }
        
    create_response = client.post("/books/", json=payload_create)

    assert create_response.status_code == 200

    book_id = create_response.json()["id"]

    # READ
    read_response = client.get(f"/books/{book_id}")

    assert read_response.status_code == 200

    # UPDATE
    payload_update = {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "price": 13.5
    }
    
    update_response = client.put(f"/books/{book_id}", json=payload_update)

    assert update_response.status_code == 200
    assert update_response.json()["title"] == "The Catcher in the Rye"
    assert update_response.json()["author"] == "J.D. Salinger"
    assert update_response.json()["price"] == 13.5

    # DELETE
    delete_response = client.delete(f"/books/{book_id}")

    assert delete_response.status_code == 200

    # VERIFY DELETION
    final_response = client.get(f"/books/{book_id}")

    assert final_response.status_code == 404