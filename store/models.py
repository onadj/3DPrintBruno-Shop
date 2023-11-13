from django.db import models
from category.models import Category
from django.urls import reverse
from accounts.models import Account
from django.db.models import Avg, Count

# Create your models here.

class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    selected_variation = models.ForeignKey('Variation', on_delete=models.SET_NULL, blank=True, null=True, related_name='variations')

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        return self.product_name

    def averageReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(average=Avg('rating'))
        avg = 0
        if reviews['average'] is not None:
            avg = float(reviews['average'])
        return avg

    def countReview(self):
        reviews = ReviewRating.objects.filter(product=self, status=True).aggregate(count=Count('id'))
        count = 0
        if reviews['count'] is not None:
            count = int(reviews['count'])
        return count

class VariationManager(models.Manager):
    def colors(self):
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        return super(VariationManager, self).filter(variation_category='size', is_active=True)
    
    def packs(self):
        return super(VariationManager, self).filter(variation_category='pack', is_active=True)
    
    def switchtypes(self):
        return super(VariationManager, self).filter(variation_category='switchtype', is_active=True)
    
    def mounting_options(self):
        return super(VariationManager, self).filter(variation_category='mounting_option', is_active=True)
    
    def individual_colors(self):
        return super(VariationManager, self).filter(variation_category='individual_color', is_active=True)
    
    def shapes(self):
        return super(VariationManager, self).filter(variation_category='shape', is_active=True)
    
    def batteries_types(self):
        return super(VariationManager, self).filter(variation_category='batteries_type', is_active=True)
    
    def sets(self):
        return super(VariationManager, self).filter(variation_category='set', is_active=True)
    
    def shelf_sizes(self):
        return super(VariationManager, self).filter(variation_category='shelf_size', is_active=True)
    
    def container_types(self):
        return super(VariationManager, self).filter(variation_category='container_type', is_active=True)
    
    def holder_sizes(self):
        return super(VariationManager, self).filter(variation_category='holder_size', is_active=True)
    
    def first_colors(self):
        return super(VariationManager, self).filter(variation_category='first_color', is_active=True)
    
    def second_colors(self):
        return super(VariationManager, self).filter(variation_category='second_color', is_active=True)
    
    def third_colors(self):
        return super(VariationManager, self).filter(variation_category='third_color', is_active=True)
    
    def fourth_colors(self):
        return super(VariationManager, self).filter(variation_category='fourth_color', is_active=True)
    
    def type_placements(self):
        return super(VariationManager, self).filter(variation_category='type_placement', is_active=True)
    
    def cage_colors(self):
        return super(VariationManager, self).filter(variation_category='cage_color', is_active=True)
    
    def cage_colors(self):
        return super(VariationManager, self).filter(variation_category='cage_color', is_active=True)
    
    def seat_colors(self):
        return super(VariationManager, self).filter(variation_category='seat_color', is_active=True)
    
    def stand_types(self):
        return super(VariationManager, self).filter(variation_category='stand_type', is_active=True)
    
    def phone_holder_types(self):
        return super(VariationManager, self).filter(variation_category='phone_holder_type', is_active=True)
    
    def keycaps_colors(self):
        return super(VariationManager, self).filter(variation_category='keycaps_color', is_active=True)
    
    def switch_colors(self):
        return super(VariationManager, self).filter(variation_category='switch_color', is_active=True)
    
    def spur_colors(self):
        return super(VariationManager, self).filter(variation_category='spur_color', is_active=True)
    
    def sprocket_colors(self):
        return super(VariationManager, self).filter(variation_category='sprocket_color', is_active=True)
    
    def screw_colors(self):
        return super(VariationManager, self).filter(variation_category='screw_color', is_active=True)
    
    def inserts(self):
        return super(VariationManager, self).filter(variation_category='insert', is_active=True)
    
    def keyboard_thicknesss(self):
        return super(VariationManager, self).filter(variation_category='keyboard_thickness', is_active=True)
    
    def laptop_thicknesss(self):
        return super(VariationManager, self).filter(variation_category='laptop_thickness', is_active=True)
    
    def drawer_sizes(self):
        return super(VariationManager, self).filter(variation_category='drawer_size', is_active=True)
    
    def him_colors(self):
        return super(VariationManager, self).filter(variation_category='him_color', is_active=True)
    

    def she_colors(self):
        return super(VariationManager, self).filter(variation_category='she_color', is_active=True)
    
    def headphone_band_widths(self):
        return super(VariationManager, self).filter(variation_category='headphone_band_width', is_active=True)
    
variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
    ('pack', 'pack'),
    ('switchtype', 'switchtype'),
    ('mounting_option', 'mounting_option'),
    ('individual_color', 'individual_color'),
    ('shape', 'shape'),
    ('batteries_type', 'batteries_type'),
    ('set', 'set'),
    ('shelf_size', 'shelf_size'),
    ('container_type', 'container_type'),
    ('holder_size', 'holder_size'),
    ('first_color', 'first_color'),
    ('second_color', 'secondary_color'),
    ('third_color', 'third_color'),
    ('fourth_color', 'fourth_color'),
    ('type_placement', 'type_placement'),
    ('cage_color', 'cage_color'),
    ('seat_color', 'seat_color'),
    ('stand_type', 'stand_type'),
    ('phone_holder_type', 'phone_holder_type'),
    ('keycaps_color', 'keycaps_color'),
    ('switch_color', 'switch_color'),
    ('spur_color', 'spur_color'),
    ('sprocket_color', 'sprocket_color'),
    ('screw_color', 'screw_color'),
    ('insert', 'insert'),
    ('keyboard_thickness', 'keyboard_thickness'),
    ('laptop_thickness', 'laptop_thickness'),
    ('drawer_size', 'drawer_size'),
    ('him_color', 'him_color'),
    ('she_color', 'she_color'),
    ('headphone_band_width', 'headphone_band_width'),

)




class Variation(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='variations')
    variation_category = models.CharField(max_length=100, choices=variation_category_choice)
    variation_value = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now=True)
    extra_cost = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    objects = VariationManager()

    def __str__(self):
        return self.variation_value

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

class ProductGallery(models.Model):
    product = models.ForeignKey(Product, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='store/products', max_length=255)

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'productgallery'
        verbose_name_plural = 'product gallery'

class ProductVideo(models.Model):
    product = models.ForeignKey(Product, related_name='videos', on_delete=models.CASCADE)
    video = models.FileField(upload_to='store/products')

    def __str__(self):
        return self.product.product_name