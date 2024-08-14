from flask import Blueprint, request, jsonify
from use_case.product.create_product import CreateProduct
from use_case.product.read_product import ReadProduct
from use_case.product.update_product import UpdateProduct
from use_case.product.delete_product import DeleteProduct

from adapter.repository.product.product_repository import ProductRepository

product_blueprint = Blueprint('product', __name__)
product_repository = ProductRepository()

@product_blueprint.route('/products', methods=['POST'])
def create_product():
    data = request.json
    create_use_case = CreateProduct(product_repository)
    new_product_dict = create_use_case.execute(data)
    
    return jsonify({
        'message': 'Product created',
        'id': new_product_dict["id"],
        'name': new_product_dict["name"],
        'code': new_product_dict["code"],
        'category': new_product_dict["category"],
        'unit_price': new_product_dict["unit_price"],
        'inventory': new_product_dict["inventory"],
        'sizes': [size["name"] for size in new_product_dict["sizes"]],
        'colors': [color["name"] for color in new_product_dict["colors"]]
    }), 201

@product_blueprint.route('/products', methods=['GET'])
def get_products():
    read_use_case = ReadProduct(product_repository)
    products_dict = read_use_case.get_all()
    if products_dict:
        return jsonify([{
            'id': product["id"],
            'name': product["name"],
            'code': product["code"],
            'category': product["category"],
            'sizes': [size["name"] for size in product["sizes"]],
            'unit_price': float(product["unit_price"]),
            'inventory': product["inventory"],
            'colos': [color["name"] for color in product["colors"]]
        } for product in products_dict])
    else:
        return []
    
@product_blueprint.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    read_use_case = ReadProduct(product_repository)
    product_dict = read_use_case.get_by_id(id)
    if product_dict:
        return jsonify({
            'id': product_dict["id"],
            'name': product_dict["name"],
            'code': product_dict["code"],
            'category': product_dict["category"],
            'sizes': [size["name"] for size in product_dict["sizes"]],
            'unit_price': float(product_dict["unit_price"]),
            'inventory': product_dict["inventory"],
            'colors': [color["name"] for color in product_dict["colors"]]
        })
    return jsonify({'message': 'Product not found'}), 404

@product_blueprint.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    update_use_case = UpdateProduct(product_repository)
    updated_product = update_use_case.execute(id, data)
    if updated_product:
        return jsonify({'message': 'Product updated'})
    return jsonify({'message': 'Product not found'}), 404

@product_blueprint.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    delete_use_case = DeleteProduct(product_repository)
    result = delete_use_case.execute(id)
    if result:
        return jsonify({'message': 'Product deleted'})
    return jsonify({'message': 'Product not found'}), 404
