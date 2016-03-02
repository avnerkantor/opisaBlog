from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User #=> for User who login
from django.template.defaultfilters import slugify
from django.utils import timezone
import datetime
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from  django.db.models import permalink


class Author(models.Model):
    name = models.CharField('שם', max_length=50)
    email = models.EmailField('דואל', unique=True)
    bio = models.TextField('ביוגרפיה')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'מחבר'
        verbose_name_plural = 'מחברים'


class Category(models.Model):
    cat_name = models.CharField('category name', max_length=50)
    cat_description = models.CharField('category description', max_length=255)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.cat_name


class Tag(models.Model):
    tag_name = models.CharField(max_length=50)
    tag_description = models.CharField(max_length=255)

    def __str__(self):
        return self.tag_name


class Post(models.Model):
    """
	Model untuk post
	"""  # choices untuk status post
    STATUS_CHOICES = (
        ('d', 'Draft'),
        ('p', 'Publish'),
        ('a', 'Archieved'),
    )


    # authors = models.ManyToManyField(Author)
    # author = models.ForeignKey('auth.User', blank=True, null=True, default=1)
    author = models.ForeignKey(Author, blank=True, null=True)
    title = models.CharField('כותרת', max_length=200, db_index=True, unique=True)
    slug = models.SlugField(max_length=200, unique=True, db_index=True, allow_unicode=True, null=True, blank=True)
    text = RichTextField('טקסט')
    created_date = models.DateTimeField(
        default=timezone.now)
    published_date = models.DateTimeField('תאריך פרסום',
                                          default=timezone.now)
    category = models.ForeignKey(Category, related_name='post_category', null=True)
    tags = models.ManyToManyField(Tag)
    status = models.CharField(max_length=1, default='d', choices=STATUS_CHOICES)

def __str__(self):
    return self.title


class Meta:
    verbose_name = 'רשומה'
    verbose_name_plural = 'רשומות'

    # def get_absolute_url(self):
    #     return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    # def get_absolute_url(self):
    #     return reverse("posts:detail", kwargs={"slug": self.slug})
