from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields
from django.db.models.fields.related import ForeignKey
from django.forms import ModelForm, Textarea, TextInput, widgets
from django.utils.safestring import mark_safe


# Create your models here.
class Settings(models.Model):
    STATUS = {
        ('True', 'yes'),
        ('False', 'no'),
    }


    tittle = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    keywords = models.CharField(max_length=200)
    company = models.CharField(max_length=30)
    addres = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    fax = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    smtpserver = models.CharField(max_length=30)
    smtpemail = models.CharField(max_length=30)
    smtppassword = models.CharField(max_length=30)
    smtpport = models.CharField(max_length=30)
    icon = models.ImageField(blank=True,upload_to='images/')
    facebook = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    aboutus = RichTextUploadingField()
    contact = RichTextUploadingField()
    references = RichTextUploadingField()
    status = models.CharField(max_length=20,choices=STATUS)
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.tittle


class ContactFormMessage(models.Model):
    STATUS = {
        ('True', 'New'),
        ('False', 'Read'),
    }


    name = models.CharField(blank=True, max_length=20)
    email = models.CharField(blank=True,max_length=50)
    subject = models.CharField(blank=True,max_length=50)
    message = models.CharField(blank=True,max_length=255)
    ip = models.CharField(blank=True,max_length=20)
    note = models.CharField(blank=True,max_length=100)
    status = models.CharField(max_length=20,choices=STATUS,default='New')
    creat_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
class ContactForm(ModelForm):
    class Meta:
        model = ContactFormMessage
        fields = ['name','email','subject','message']
        widgets = {
            'name': TextInput(attrs={'class':'input','placeholder':'Name & Surname'}),
            'email': TextInput(attrs={'class':'input','placeholder':'email'}),
            'subject': TextInput(attrs={'class':'input','placeholder':'subject'}),
            'message': Textarea(attrs={'class':'input','placeholder':'message'}),
        }
     
class UserProfileInfo(models.Model):

    user=models.OneToOneField(User,related_name='userprofile', on_delete=models.CASCADE)
    AUTH_PROFILE_MODULE = 'app.UserProfile'
    phone = models.CharField(max_length=50,blank=True)
    city = models.CharField(max_length=150,blank=True)
    country = models.CharField(max_length=50,blank=True)
    image = models.ImageField(User,blank=True,upload_to='images/users/')
    address=models.CharField(max_length=40)
    def __str__(self):
        return self.user.username
    def user_name(self):
        return self.user.username+' '+ self.user.first_name
    def image_tag(self):
        return mark_safe('<img src="{}" height="30"/>'.format(self.image.url))
    image_tag.short_description = 'Image'       
class UserProfileInfoForm(ModelForm):
    class Meta:
        model = UserProfileInfo
        fields = ['user','phone','city','country','image','address']




