from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Updated"))


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="library_books"
    )
    cover_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    uploaded_on = models.DateTimeField(auto_now_add=True)
    returned_on = models.DateTimeField(auto_now=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='books_like', blank=True)

    class Meta:
        ordering = ["-uploaded_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE,
                             related_name="reviews")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    uploaded_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["uploaded_on"]

    def __str__(self):
        return f"Reviews {self.body} by {self.name}"
