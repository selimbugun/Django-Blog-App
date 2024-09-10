from venv import logger
from django.db import models
from django.contrib.auth.models import User
import os
from PIL import Image
from django.utils.text import slugify
from unidecode import unidecode


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.name))

        super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
    


def resize_image(image_file, target_width, target_height):
    try:
        img = Image.open(image_file)
        img = img.convert('RGB')  # Görseli RGB formatına dönüştür
        # Orantılı olarak boyutlandırma
        width, height = img.size
        aspect_ratio = width / height
        if aspect_ratio > (target_width / target_height):
            new_height = int(target_width / aspect_ratio)
            img = img.resize((target_width, new_height), Image.LANCZOS)
        else:
            new_width = int(target_height * aspect_ratio)
            img = img.resize((new_width, target_height), Image.LANCZOS)

        # Görseli kaydet
        img.save(image_file, optimize=True, quality=85)  # Yüksek kalite için quality değerini ayarlayın

    except IOError as err:
        logger.error(f'Yeniden boyutlandırılamadı', err)
        raise ValueError('Desteklenmeyen görüntü formatı')

    



class Post(models.Model):
    title = models.CharField(max_length=100)
    mini_content = models.CharField(max_length=60, default="")
    content = models.TextField()
    categories = models.ManyToManyField(Category)
    image = models.ImageField(upload_to='images')
    slug = models.SlugField(default="", unique=True, null=False, blank=True, db_index=True)

    publish_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)

    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title
    

    def save(self, *args, **kwargs):
        if self.image:
            if not os.path.exists(self.image.path):
                try:
                    resize_image(self.image, 310, 310)
                except ValueError as err:
                    logger.error(f"Görüntü yeniden boyutlandırılaamdı: {err}")
                except Exception as err:
                    logger.error(f"Görüntü kaydedilirken hata oluştu: {err}")

        if not self.slug or self.slug:
                self.slug = slugify(unidecode(self.title))

        super().save(*args, **kwargs)


class Projects(models.Model):
    title = models.CharField(max_length=50)
    mini_description = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')
    slug = models.SlugField(unique=True, default ="", null=False, blank= True, db_index=True)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug or self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)


class Contact(models.Model):
    username = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    subject = models.CharField(max_length=100, null=False, blank=False)
    message = models.TextField(null=False, blank=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.subject
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
        
