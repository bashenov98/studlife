from django.db import models

from users.models import CustomUser, Organization
from utils.validators import extension_validator, file_size_validator
# Create your models here.

<<<<<<< HEAD
=======

>>>>>>> asd
class PostManager(models.Manager):
    def for_user(self, user):
        return self.filter(owner=user)

<<<<<<< HEAD
=======

>>>>>>> asd
class Post(models.Model):
    name = models.CharField(max_length=150)
    text = models.TextField()

    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
<<<<<<< HEAD
    object = PostManager()
=======
    objects = PostManager()
>>>>>>> asd

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"

<<<<<<< HEAD

    def __str__(self):
        return self.name

=======
    def __str__(self):
        return self.name


>>>>>>> asd
class EventManager(models.Manager):
    def for_organization(self, organization1):
        return self.filter(organization=organization1)

<<<<<<< HEAD
=======

>>>>>>> asd
class Event(models.Model):
    name = models.CharField(max_length=150)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    date = models.DateTimeField()
    description = models.TextField()
    poster = models.ImageField(upload_to='media/images',
                              validators=[extension_validator,
                                          file_size_validator],
                              null=True, blank=True)
    objects = EventManager()

    def __str__(self):
        return f'{self.name}: {self.date}'

<<<<<<< HEAD
=======

>>>>>>> asd
class Comment(models.Model):
    message = models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    class Meta:
        abstract = True

<<<<<<< HEAD
=======

>>>>>>> asd
class CommentPostManager(models.Manager):
    def get_comments_of_post(self, post):
        return self.filter(post=post)

<<<<<<< HEAD
=======

>>>>>>> asd
class CommentPost(Comment):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')

    objects = CommentPostManager()

    def __str__(self):
        return f'{self.post.name}: {self.message}'



