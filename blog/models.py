from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.


class Tag(models.Model):
    caption = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.caption}"


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Post(models.Model):
    title = models.CharField(max_length=50)
    excerpt = models.CharField(max_length=50)
    # image_name = models.ImageField(max_length=50)
    image_name = models.CharField(max_length=50)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinValueValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="posts")
    slug = models.SlugField(default="", null=False, db_index=True,unique=True)
    captions = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return f"{self.title} - Posted by: {self.author}, at: {self.date}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])
