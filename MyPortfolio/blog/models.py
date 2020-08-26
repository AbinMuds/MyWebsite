from django.db import models
from django.urls import reverse
from django.utils import timezone

# Post model
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    post_image = models.ImageField(upload_to='pics/',blank=False,null=True)
    link_to_code = models.URLField(blank=True)
    date_of_creation = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def approve_comment(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})

    def __str__(self):
        return self.title

# comment model
class Comment(models.Model):
    post = models.ForeignKey('blog.Post',related_name='comments',on_delete=models.CASCADE)
    author = models.CharField(max_length = 250)
    text = models.TextField()
    date_of_creation = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()
# takes to post list after the comment is posted
    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text

# contact for other any users to give their Feedbacks
class Contact(models.Model):
    username = models.CharField(max_length=250,blank=False)
    portfolio_site = models.URLField(blank=True)
    message = models.TextField(blank=False)
    email = models.EmailField(blank=True)

    def __str__(self):
        return self.username
