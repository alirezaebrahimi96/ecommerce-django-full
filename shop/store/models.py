from django.db import models
from taggit.managers import TaggableManager
from django.urls import reverse



class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    parent = models.ForeignKey('self',
                                on_delete=models.CASCADE,
                                null=True,
                                blank=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("store:category", kwargs={"name": self.name})



class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=500, default="Empty description.")    
    category = models.ManyToManyField(Category, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    tags = TaggableManager(blank=True)
    picture = models.ImageField(upload_to="products/images", null=True, blank=True)
    price = models.DecimalField(decimal_places=2, max_digits=20, default=0)
    quantity = models.IntegerField(default=10)
    featured = models.BooleanField(default=False)       
    
    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name

    @property
    def is_featured(self):
        return self.featured

    @property
    def is_available(self):
        return self.quantity > 0