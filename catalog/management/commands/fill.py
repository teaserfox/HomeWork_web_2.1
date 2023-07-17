from django.core.management import BaseCommand

from catalog.templates.catalog.models.Category import Category
from catalog.templates.catalog.models.Products import Product


class Products:
    pass


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Список категорий для добавления
        categories = [
            {'name': 'Классическая зарубежная проза'},
            {'name': 'Исторический детектив'},
            {'name': 'Классическая отечественная проза'},
            {'name': 'Личная эффективность, мотивация'}
        ]

        # Очистка таблицы Category
        Category.objects.all().delete()

        # Список экземпляров класса Category
        categories_for_create = []
        for category in categories:
            categories_for_create.append(Category(**category))

        # Добавление категорий в базу данных
        Category.objects.bulk_create(categories_for_create)

        # Список продуктов для добавления в БД
        products = [{'name': 'Повелитель мух',
                     'purchase_price': 276,
                     'category': categories_for_create[0]},  # Классическая зарубежная проза

                    {'name': 'Убийство в "Восточном экспрессе"',
                     'purchase_price': 309,
                     'category': categories_for_create[1]},  # Исторический детектив

                    {'name': 'Идиот',
                     'purchase_price': 329,
                     'category': categories_for_create[2]},  # Классическая отечественная проза

                    {'name': 'Тонкое искусство пофигизма: Парадоксальный способ жить счастливо',
                     'purchase_price': 587,
                     'category': categories_for_create[3]}]  # Личная эффективность, мотивация

        # Очистка таблицы Product
        Product.objects.all().delete()

        # Список экземпляров класса Product
        products_for_create = []
        for product in products:
            products_for_create.append(Product(**product))

        # Добавление продуктов в базу данных
        Product.objects.bulk_create(products_for_create)
