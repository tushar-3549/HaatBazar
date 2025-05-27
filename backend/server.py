from fastapi import FastAPI, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import json

from sql_connection import get_sql_connection
import products
# import orders
import uom

app = FastAPI()

# CORS Middleware to allow frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Database connection

connection = get_sql_connection()

# Endpoint: Get UOM

@app.get("/getUOM")
def get_uom():
    response = uom.get_uoms(connection)
    return JSONResponse(content=response)

# Endpoint: Get all products
@app.get("/getProducts")
def get_products():
    response = products.get_all_products(connection)
    return JSONResponse(content=response)

# Endpoint: Insert new product
@app.post("/insertProduct")
def insert_product(data: str = Form(...)):
    request_payload = json.loads(data)
    product_id = products.insert_new_product(connection, request_payload)
    return JSONResponse(content={"product_id": product_id})

# Endpoint: Get all orders

# @app.get("/getAllOrders")
# def get_all_orders():
#     response = orders.get_all_orders(connection)
#     return JSONResponse(content=response)

# Endpoint: Insert new order

# @app.post("/insertOrder")
# def insert_order(data: str = Form(...)):
#     request_payload = json.loads(data)
#     order_id = orders.insert_order(connection, request_payload)
#     return JSONResponse(content={"order_id": order_id})

# Endpoint: Delete a product
@app.post("/deleteProduct")
def delete_product(product_id: str = Form(...)):
    return_id = products.delete_product(connection, product_id)
    return JSONResponse(content={"product_id": return_id})


# Endpoint: Update/ Edit a product

@app.post("/updateProduct")
def update_product(data: str = Form(...)):
    request_payload = json.loads(data)
    success = products.update_product(connection, request_payload)
    return JSONResponse(content={"updated": success})


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("server:app", host="0.0.0.0", port=5000, reload=True)
