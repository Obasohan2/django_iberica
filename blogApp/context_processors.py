from .models import Category


def get_categories(request):
    categories = Category.objects.all()
    # This context processor retrieves all categories from the database and edit templates in setting.py
    return dict(categories=categories)