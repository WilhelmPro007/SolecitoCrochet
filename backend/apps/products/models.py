from django.db import models
from django.db.models.signals import post_migrate
from django.dispatch import receiver

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    @classmethod
    def get_default_categories(cls):
        return [
            {
                'name': 'Amigurumis',
                'description': 'Muñecos y figuras tejidas en crochet'
            },
            {
                'name': 'Accesorios',
                'description': 'Gorros, bufandas, guantes y otros accesorios tejidos'
            },
            {
                'name': 'Decoración',
                'description': 'Artículos decorativos para el hogar'
            },
            {
                'name': 'Ropa',
                'description': 'Prendas de vestir tejidas a crochet'
            },
            {
                'name': 'Bebés',
                'description': 'Artículos tejidos para bebés y niños pequeños'
            }
        ]

@receiver(post_migrate)
def create_default_categories(sender, **kwargs):
    if sender.name == 'products':  # Solo ejecutar para la app 'products'
        Category = sender.get_model('Category')
        if Category.objects.count() == 0:  # Solo crear si no existen categorías
            for category_data in Category.get_default_categories():
                Category.objects.create(**category_data)

class ProductImage(models.Model):
    product = models.ForeignKey('Product', related_name='additional_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products/additional/')
    order = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"Imagen {self.order} de {self.product.name}"

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', verbose_name='Imagen principal')  # Imagen principal
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    @property
    def all_images(self):
        """Retorna todas las imágenes del producto, incluyendo la principal"""
        return [self.image] + list(self.additional_images.all().values_list('image', flat=True))
