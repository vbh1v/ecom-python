from models.category import Category

class CategoryService:
    def get_all_categories(self):
        return Category.get_all()