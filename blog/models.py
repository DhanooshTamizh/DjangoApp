from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Posts(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField()
	date_posted= models.DateTimeField(default=timezone.now)
	author = models.ForeignKey(User,on_delete=models.CASCADE)
	likes = models.ManyToManyField(User, related_name='postl')

	git_link=models.CharField(max_length=50,default='github')

	def total_likes(self):
		return self.likes.count()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('blog-post-detail',kwargs={'pk': self.pk})


class Comment(models.Model):
	post=models.ForeignKey(Posts,on_delete=models.CASCADE)
	user=models.ForeignKey(User,on_delete=models.CASCADE)
	comments=models.CharField(max_length=100, default='comment')

	def __str__(self):
		return '{}-{}'.format(self.post.title,str(self.user.username))