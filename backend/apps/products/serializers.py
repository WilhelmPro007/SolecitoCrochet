from rest_framework import serializers
from .models import Product, Category, ProductImage

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description']

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id', 'image', 'order']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    additional_images = ProductImageSerializer(many=True, read_only=True)
    uploaded_images = serializers.ListField(
        child=serializers.ImageField(max_length=1000000, allow_empty_file=False, use_url=False),
        write_only=True,
        required=False
    )

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 
                'category_name', 'stock', 'image', 'is_active', 
                'additional_images', 'uploaded_images']

    def create(self, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        product = Product.objects.create(**validated_data)
        
        for order, image in enumerate(uploaded_images):
            ProductImage.objects.create(
                product=product,
                image=image,
                order=order
            )
        
        return product

    def update(self, instance, validated_data):
        uploaded_images = validated_data.pop('uploaded_images', [])
        
        # Actualizar los campos del producto
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        # Añadir nuevas imágenes
        current_order = instance.additional_images.count()
        for order, image in enumerate(uploaded_images, start=current_order):
            ProductImage.objects.create(
                product=instance,
                image=image,
                order=order
            )

        return instance 