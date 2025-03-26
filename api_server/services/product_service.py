from models.product import Product

class ProductService:
    def get_products_by_category(self, category_id):
        return Product.get_by_category(category_id)