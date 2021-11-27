from django.db import models

# Create your models here.

class Category(models.Model):
    STATUS = {
        ('True', 'yes'),
        ('False', 'no'),
    }

    tittle = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=20,choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle
class Product(models.Model):
    STATUS = {
        ('True', 'yes'),
        ('False', 'no'),
    }
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.FloatField()
    amount = models.IntegerField()
    details = models.TextField()

    tittle = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    image = models.ImageField(blank=True,upload_to='images/')
    status = models.CharField(max_length=20,choices=STATUS)
    slug = models.SlugField()
    parent = models.ForeignKey('self',blank=True,null=True,related_name='children',on_delete=models.CASCADE)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.tittle