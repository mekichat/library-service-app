import requests

import pytest

pytestmark = pytest.mark.e2e

BOOK_SERVICE = "http://localhost:8000"
ORDER_SERVICE = "http://localhost:8080"


def test_create_book_and_order_flow():
    # 1. Create book
    book_payload = {
        "title": "Dune",
        "author": "Frank Herbert",
        "price": 25.5
    }

    book_res = requests.post(f"{BOOK_SERVICE}/books", json=book_payload)
    assert book_res.status_code == 200
    book_id = book_res.json()["id"]

    # 2. Create order
    order_payload = {
        "book_id": book_id,
        "quantity": 1
    }

    order_res = requests.post(f"{ORDER_SERVICE}/orders", json=order_payload)
    
    print(order_res.status_code)
    print(order_res.text)
    
    assert order_res.status_code == 201
    assert "id" in order_res.json()
    order_id = order_res.json()["id"]

    # 3. Verify order exists
    get_res = requests.get(f"{ORDER_SERVICE}/orders/{order_id}")
    assert get_res.status_code == 200

    # 4. Cleanup
    requests.delete(f"{ORDER_SERVICE}/orders/{order_id}")