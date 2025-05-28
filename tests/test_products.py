from fastapi.testclient import TestClient
from backend.server import app
import json

client = TestClient(app)

def test_get_products():
    res = client.get('/getProducts')
    assert res.status_code == 200
    assert isinstance(res.json(), list)

def test_insert_product():
    new_product = {
        'product_name': "Test product",
        'uom_id': 1,
        'price_per_unit': 60
    }

    response = client.post("/insertProduct", data = {
        "data": json.dumps(new_product)
    })

    assert response.status_code == 200
    data = response.json()
    assert "product_id" in data 
    assert isinstance(data["product_id"], int)


def test_update_product():
    # First insert
    new_product = {
        "product_name": "Update Test",
        "uom_id": 1,
        "price_per_unit": 25
    }
    insert_resp = client.post("/insertProduct", data={
        "data": json.dumps(new_product)
    })
    product_id = insert_resp.json()["product_id"]

    updated_product = {
        "product_id": product_id,
        "product_name": "Updated Product",
        "uom_id": 1,
        "price_per_unit": 45
    }

    response = client.post("/updateProduct", data={
        "data": json.dumps(updated_product)
    })

    assert response.status_code == 200
    assert response.json()["updated"] is True



def test_delete_product():
    # Insert product to delete
    new_product = {
        "product_name": "To Delete",
        "uom_id": 1,
        "price_per_unit": 20
    }

    insert_res = client.post("/insertProduct", data={
        "data": json.dumps(new_product)
    })
    product_id = insert_res.json()["product_id"]
    response = client.post("/deleteProduct", data={"product_id": product_id})
    assert response.status_code == 200
    assert int(response.json()["product_id"]) == product_id

