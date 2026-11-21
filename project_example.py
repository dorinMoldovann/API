#import and Flask app initialization
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# List of products (Instead of a database for the sake of simplicity)
products = [
    {"id": 1, "name": "Laptop", "price": 1500},
    {"id": 2, "name": "Telefon", "price": 800},
    {"id": 3, "name": "Mouse", "price": 20}
]

#Response from GET for main page
@app.route('/')
def index():
    return render_template('index.html', products=products)


# Răspunde la POST pentru adăugarea unui produs

@app.route('/add_product', methods=['POST'])
def add_product():
    name = request.form.get('name')

    price = request.form.get('price')

    #Add product

    new_product = {

        "id": len(products) + 1,

        "name": name,

        "price": float(price)

    }

    products.append(new_product)

    return render_template('index.html', products=products)

# Răspuns GET pentru a returna toate produsele
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products), 200


# Răspuns la DELETE pentru a șterge un produs
# /products/{id}

@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    product = next((p for p in products if p["id"] == id), None)
    if product:
        products.remove(product)
        return jsonify({"message": "Product deleted"}), 200
    return jsonify({"message": "Product not found"}), 404

if __name__ == '__main__':
    app.run(debug = True)
