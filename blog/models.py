from django.db import models
from django.core.validators import MinLengthValidator, MinValueValidator
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
    image = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now=True)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, null=True, related_name="posts")
    slug = models.SlugField(default="", null=False, db_index=True, unique=True)
    captions = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return f"{self.title} - Posted by: {self.author}, at: {self.date}"

    def get_absolute_url(self):
        return reverse("book_detail", args=[self.slug])


class Comment(models.Model):
    user_name = models.CharField(max_length=50)
    comment_text = models.TextField(
        max_length=200, validators=[MinLengthValidator(10)])
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, null=True, related_name="comments")

    def __str__(self):
        return f"{self.user_name.capitalize} commented {self.post.title} "
