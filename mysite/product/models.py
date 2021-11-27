
from typing import Reversible
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.safestring import mark_safe
from mptt.models import MPTTModel, TreeForeignKey
from django.forms import ModelForm
from django.contrib.auth.models import User
from django.urls import reverse




# Create your models here.
class Category(MPTTModel):
    STATUS = {
        ('True', 'yes'),
        ('False', 'no'),
    }

    tittle = models.CharField(max_length=30)
    description = models.CharField(blank=True ,max_length=200)
    keywords = models.CharField(blank=True ,max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=20,choices=STATUS)
    slug = models.SlugField(null=False,unique=True)
    parent = TreeForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    class MPTTMeta:
        
        order_insertion_by = ['tittle']

    def __str__(self):
        full_path = [self.tittle]
        x=self.parent
        while x is not None:
            full_path.append(x.tittle)
            x=x.parent
        return '>>' .join(full_path[::-1])

    def auto_slug(self):
        return reverse('article_detail', kwargs={'slug':self.slug})


class Product(models.Model):
    STATUS = {
        ('True', 'yes'),
        ('False', 'no'),
    }
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()
    amount = models.IntegerField()
    details = RichTextUploadingField()

    tittle = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=20,choices=STATUS)
    slug = models.SlugField(blank=True,max_length=50)
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tittle
    def image_tag(self):
        return mark_safe('<img src="{}" height="30"/>'.format(self.image.url))
    image_tag.short_description = 'Image'
    



    



    

class Images(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    tittle = models.CharField(max_length=70,blank=True)
    image = models.ImageField(blank=True,upload_to ='images/')
    def __str__(self):
        return self.tittle
class Coment(models.Model):
    STATUS = {
        ('New','Yeni'),
        ('True', 'yes'),
        ('False', 'no'),
    }
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    subject = models.CharField(max_length=50,blank=True)
    comment = models.TextField(max_length=200,blank=True)

    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, blank=True,default='New')
    ip = models.CharField(max_length=20,blank=True)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.subject
class CommentForm(ModelForm):
    class Meta:
        model = Coment
        fields = ['subject','comment','rate']


class ShopCart(models.Model):
    
    user=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    product=models.ForeignKey(Product,on_delete=models.SET_NULL,null=True)
    quantity=models.IntegerField()
    def __str__(self):
        return str(self.product)
    @property
    def __str__(self):
        return self.product.tittle
    @property
    def amount(self):
        return self.quantity*self.product.price
    @property
    def price(self):
        return  self.product.price
class ShopCartForm(ModelForm):
    class Meta:
        model=ShopCart
        fields = ['quantity']
