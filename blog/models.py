from django.db import models
from django.utils.text import slugify

from accounts.models import CustomUser
# Create your models here.

class CreateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Category(models.Model):
    title = models.CharField(max_length= 256)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'

class Post(CreateTime):
    ACTIVE = 'active'
    DRAFT = 'draft'
    CHOICES = (
        (ACTIVE, 'Active'),
        (DRAFT, 'Draft'),
    )
    title = models.CharField(max_length=256)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    status = models.CharField(max_length=256, choices=CHOICES, default=ACTIVE)
    image = models.ImageField(upload_to = 'uploads/', blank = True, null = True)
    category = models.ForeignKey(Category, on_delete= models.CASCADE, related_name='posts')
    author = models.ForeignKey(CustomUser, on_delete= models.CASCADE, related_name='feeds')

    def __str__(self) -> str:
        return self.title
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['-created_at']

class Comment(CreateTime):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=256)
    email = models.EmailField()
    body = models.TextField()


    def __str__(self) -> str:
        return self.name

        