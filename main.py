from fastapi import FastAPI
from models import Product


app = FastAPI()


@app.get("/")
def greet():
    return "Hello, World!"


@app.get("/health")
def call():
    return "OK"


products = [
    Product(
        id=1,
        name="Laptop",
        description="A high-performance laptop",
        price=999.99,
        quantity=10,
    ),
    Product(
        id=2,
        name="Smartphone",
        description="A latest model smartphone",
        price=699.99,
        quantity=25,
    ),
]


@app.get("/products")
def get_all_products():
    return products


@app.get("/product/{id}")
def get_product_by_id(id: int):
    for product in products:
        if product.id == id:
            return product
    return {"error": "Product not found"}


@app.post("/product")
def add_product(product: Product):
    products.append()


if __name__ == "__main__":
    greet()
