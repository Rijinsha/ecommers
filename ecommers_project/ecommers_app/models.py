from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=300,unique=True)  #unique using the name consider only unque value
    # when a name is creted tha time , automaticaly url created using slug
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    # img are uploaded to 'categories'folder/directory
    image=models.ImageField(upload_to='category',blank=True)

    class Metta:
        ordering=('name',)
        verbose_name='category'
        verbose_name_plural='categories'
    def get_url(self):
        return reverse('ecommers_app:product_by_category',args=[self.slug])

    def __str__(self):
        return '{}'.format(self.name)

#product feild
class Product(models.Model):
    name = models.CharField(max_length=300, unique=True)
    slug=models.SlugField(max_length=250,unique=True)
    description=models.TextField(blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2)
    category=models.ForeignKey(Category,on_delete=models.CASCADE) #cascade using the previous values delete and new add
    image= models.ImageField(upload_to='product', blank=True)
    stock=models.IntegerField()
    available=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now=True)
    # detail
    def get_url(self):
        return reverse('ecommers_app:prodCatdetail',args=[self.category.slug,self.slug])

    class Metta:
        ordering=('name',)
        verbose_name='product'
        verbose_name_plural='products'

    def __str__(self):
        return '{}'.format(self.name)




