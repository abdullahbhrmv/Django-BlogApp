from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def __str__(self):
        return f"{self.name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)

class Blog(models.Model):
    blog_name = models.CharField(max_length=200)
    desc = RichTextField()
    image = models.ImageField(upload_to="blogs")
    homepage = models.BooleanField(default=False)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)
    categories = models.ManyToManyField(Category)

    def __str__(self):
        return f"{self.blog_name}"
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.blog_name)
        super().save(*args, **kwargs)
