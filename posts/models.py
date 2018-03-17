from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.
class Category(models.Model):
	name = models.CharField(max_length=90)
	
	def __str__(self):
		return "%s" % (self.name)
		
	class Meta:
		verbose_name_plural = 'Categories'
	
class Tag(models.Model):
	name = models.CharField(max_length=90, blank=True, null=True)
	
	def __str__(self):
		return "%s" % (self.name)
	
class Post(models.Model):
	title = models.CharField(max_length=100)
	subtitle = models.CharField(max_length=100)
	image = models.ImageField(upload_to='static/images/posts', null=True, blank=True)
	slug = models.SlugField(max_length=99)
	date_added = models.DateTimeField(default=timezone.now)
	author = models.CharField(max_length=60, default='Hunter Krieger')
	body = RichTextField()
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	tags = models.ManyToManyField(Tag)
	published = models.BooleanField(default=False)	
	date_published = models.DateTimeField(null=True, blank=True)
	date_updated = models.DateTimeField(null=True, blank=True)
	
	def __str__(self):
		return "%s (%s)" % (self.title, self.date_added)