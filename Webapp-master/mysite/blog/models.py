from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from taggit.managers import TaggableManager

class Post(models.Model):
    STATUS_CHOISES=(('draft','Draft'),('published','Published'),)

    title=models.CharField(max_length=250,verbose_name='Post name')
    slug=models.SlugField(max_length=250,unique_for_date='publish')
    author=models.ForeignKey(User,on_delete=models.CASCADE, related_name='blog_posts',verbose_name='Author')
    short_description=models.CharField(max_length=400,verbose_name='Description')
    tags = TaggableManager(blank=True)
    publish=models.DateTimeField(verbose_name='Publish date', default=timezone.now)
    created = models.DateTimeField(auto_now_add=True, verbose_name='Create date')
    updated = models.DateTimeField(auto_now=True, verbose_name='Update')
    status=models.CharField(max_length=10, choices=STATUS_CHOISES,default='draft')
    image=models.ImageField(upload_to='porodact_images/',verbose_name='Image',blank=False)

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:post_detail',args=[self.publish.year,
                                                self.publish.month,
                                                self.publish.day,
                                                self.slug])

def save_images(instance,filename):
    post_id=instance.post.id
    return 'gallery_images/{}/{}'.format(post_id,filename)

class PostPoint(models.Model):
    post_header = models.CharField(max_length=250, default='Header')
    post=models.ForeignKey(Post,on_delete=models.CASCADE,default=None)
    post_point_text=models.TextField(verbose_name='Post point')
    post_images = models.ImageField(upload_to=save_images, verbose_name='Image point', blank=True,)
    def __str__(self):
        return 'Post point {}'.format(self.post.title)

class Comment(models.Model):
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering=('created',)

    def __str__(self):
        return 'Коментарь {} про {}'.format(self.name, self.post)

class Tag(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class TagModel(models.Model):
    title = models.CharField(max_length=100)
    tags = models.ManyToManyField(Tag)
    def __str__(self):
        return self.title

class Trip(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.CharField(max_length=255, blank=True)
    def __str__(self):
        return self.name